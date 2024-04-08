#!/usr/bin/env python3
"""test client"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized_class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from client import GithubOrgClient


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
                     [(org_payload, repos_payload, expected_repos, apache2_repos)])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up test class"""
        cls.get_patcher = patch('client.requests.get')

        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            org_payload,  # Mock the response for org payload
            repos_payload,  # Mock the response for repos payload
            repos_payload,  # Mock the response for repos payload for Apache2 license check
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down test class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method"""

        org_name = self.org_payload['login']
        expected_repos_names = [repo['name'] for repo in self.expected_repos]

        org_client = GithubOrgClient(org_name)
        res1 = org_client.public_repos()
        res2 = org_client.public_repos()

        self.mock_get.assert_called_with(f'https://api.github.com/orgs/{org_name}/repos')
        self.assertEqual(res1, expected_repos_names)
        self.assertEqual(res2, expected_repos_names)

    def test_has_license_apache2(self):
        """Test has_license method for Apache2 license"""

        org_name = self.org_payload['login']
        org_client = GithubOrgClient(org_name)

        for repo in self.apache2_repos:
            self.assertTrue(org_client.has_license(repo, 'apache-2.0'))


if __name__ == '__main__':
    unittest.main()
