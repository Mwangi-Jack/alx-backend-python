#!/usr/bin/env python3
"""Test client"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """This class contains the methods to test client"""

    @parameterized.expand([
        ('google', {'repos_url': 'https://api.github.com/orgs/google'}),
        ('abc', {'repos_url': 'https://api.github.com/orgs/abc'})])
    @patch('client.get_json')
    def test_org(self, org, expected_value, mock_get_json):
        """
        This method tests that GithubOrgClient.org returns
        the correct value
        """
        mock_get_json.return_value = expected_value
        client = GithubOrgClient(org)
        result = client.org
        self.assertEqual(result, expected_value)
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org}'
            )


if __name__ == '__main__':
    unittest.main()
