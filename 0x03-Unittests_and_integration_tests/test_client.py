#!/usr/bin/env python3
"""
A test module for the client module
"""
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD

GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for the GithubOrgClient class
    """
    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('client.get_json')
    def test_org(self, org, mock_json):
        """Tests that GithubOrgClient.org returns the correct value
        """
        url = f'https://api.github.com/orgs/{org}'
        test = GithubOrgClient(org)
        test.org()
        mock_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """test for expected results based on mocked payload
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': 'https://api.github.com/users/google/repos'
                }
            self.assertEqual(GithubOrgClient('google')._public_repos_url,
                             'https://api.github.com/users/google/repos')

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """test that the list of repos is expected for a chosen payload
        """
        payload = [{'name': 'Google'}, {'name': 'ABC'}]
        mock_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pub:
            mock_pub.return_value = 'world'
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "ABC"])

            mock_pub.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, key, expected):
        """tests if a repo has a licence
        """
        res = GithubOrgClient.has_license(repo, key)
        self.assertEqual(res, expected)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'],
                     TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Testing in an integration test.
    Only mock code that sends external requests
    """
    @classmethod
    def setUpClass(cls):
        """setup method for the class
        """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch('requests.get', side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """teardown method for the class
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test public repos """
        self.assertEqual(
            GithubOrgClient('google').public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self):
        """test public with license"""
        self.assertEqual(
            GithubOrgClient('google').public_repos(license='apache-2.0'),
            self.apache2_repos,
        )
