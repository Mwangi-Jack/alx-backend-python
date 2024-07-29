#!/usr/bin/env python3
"""Test client"""

import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """
        This method tests the _public_repos_url method of the client
        """
        expected_org = {
            'repos_url': 'https://api.github.com/orgs/google/repos'
            }

        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = expected_org
            client = GithubOrgClient('google')
            result = client._public_repos_url

            self.assertEqual(result, expected_org['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        This method test the public_repos method of GithubOrgClient class
        """
        repos_payload = [{'name': 'repo1', 'license': {'key': 'mit'}},
                         {'name': 'repo2', 'license': {'key': 'mit'}},
                         {'name': 'repo3', 'license': {'key': 'mit'}}
                         ]
        mock_get_json.return_value = repos_payload

        expected_repos = ['repo1', 'repo2', 'repo3']
        public_repos_url = 'https://api.github.com/orgs/google/repos'

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = public_repos_url
            client = GithubOrgClient('google')
            result = client.public_repos()

            self.assertEqual(result, expected_repos)
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(public_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_licese(self, test_repo, test_license, expected_value):
        """This method tests 'has_lisence' method of GithubOrgClient"""
        result = GithubOrgClient.has_license(test_repo, test_license)

        self.assertEqual(result, expected_value)


if __name__ == '__main__':
    unittest.main()
