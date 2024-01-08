#!/usr/bin/env python3
"""
A test module for the client module
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized

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
