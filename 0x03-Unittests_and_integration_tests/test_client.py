#!/usr/bin/env python3
"""Test client"""

import unittest
import requests
from unittest.mock import patch, PropertyMock, Mock
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class # type: ignore
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
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False)
        ])
    def test_has_license(self, repo, license_key, expected_value):
        """This method tests 'has_lisence' method of GithubOrgClient"""
        result = GithubOrgClient.has_license(repo, license_key)

        self.assertEqual(result, expected_value)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up mock for requests.get and configure the return values based on the URL"""
        cls.get_patcher = patch('requests.get', autospec=True)
        cls.mock_get = cls.get_patcher.start()

        # Set the side_effect for the mock
        def get_json_mock(url):
            if url == GithubOrgClient.ORG_URL.format(org='google'):
                return cls.org_payload
            elif url == cls.org_payload['repos_url']:
                return cls.repos_payload
            return None

        cls.mock_get.return_value = Mock()
        cls.mock_get.return_value.json.side_effect = get_json_mock

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos method"""
        client = GithubOrgClient('google')
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test GithubOrgClient.public_repos method with a license filter"""
        client = GithubOrgClient('google')
        repos = client.public_repos(license='apache-2.0')
        self.assertEqual(repos, self.apache2_repos)

if __name__ == '__main__':
    unittest.main()

