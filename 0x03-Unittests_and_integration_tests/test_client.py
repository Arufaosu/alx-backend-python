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
            cls.org_payload,  # Mock the response for org payload
            cls.repos_payload,  # Mock the response for repos payload
            cls.repos_payload,  # Mock the response for repos payload for Apache2 license check
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
        result = org_client.public_repos()

        self.mock_get.assert_called_with(f'https://api.github.com/orgs/{org_name}/repos')
        self.assertEqual(result, expected_repos_names)

    def test_public_repos_with_license(self):
        """Test public_repos method with license"""

        org_name = self.org_payload['login']
        expected_repos_names = [repo['name'] for repo in self.apache2_repos]

        org_client = GithubOrgClient(org_name)
        result = org_client.public_repos(license="apache-2.0")

        self.mock_get.assert_called_with(f'https://api.github.com/orgs/{org_name}/repos')
        self.assertEqual(result, expected_repos_names)


if __name__ == '__main__':
    unittest.main()
