#!/usr/bin/env python3
"""test client"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """tests for GithubOrgClient class"""

    @parameterized.expand([('google',), ('abc',)])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test GithubOrgClient.org method"""

        expected_response = {org_name: 'Available'}
        mock_get_json.return_value = expected_response

        instance = GithubOrgClient(org_name)

        res1 = instance.org
        res2 = instance.org

        url = f'https://api.github.com/orgs/{org_name}'

        mock_get_json.assert_called_once_with(url)

        self.assertEqual(res1, res2)
        self.assertEqual(res1, expected_response)

    def test_public_repos_url(self):
        """test public_repos_url method"""

        with patch('client.GithubOrgClient.org', new_callable=PropertyMock)\
                as org_mock:
            repos = 'https://github.com/org/test/repo'

            org_mock.return_value = {'repos_url': repos}

            org_client = GithubOrgClient('test')
            res = org_client._public_repos_url

            self.assertEqual(res, repos)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test public_repos method"""
        repos_names = ['Tic_Tac_Toe_Python', 'alx-backend', 'simple_shell']
        repos = [{'name': name} for name in repos_names]

        mock_get_json.return_value = repos

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'https://github.com/test'

            org_client = GithubOrgClient('test')
            res1 = org_client.public_repos()
            res2 = org_client.public_repos()

            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

            self.assertEqual(res1, res2)
            self.assertEqual(res1, repos_names)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_response):
        """test the static method"""

        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected_response)
