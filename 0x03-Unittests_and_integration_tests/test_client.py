#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json', return_value={'login': 'mocked_org'})
    def test_org(self, org_name, mock_get_json):
        """
        Test the GithubOrgClient.org method with different organization names.
        """
        client = GithubOrgClient(org_name)
        org_info = client.org
        self.assertEqual(org_info, {'login': 'mocked_org'})
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

if __name__ == "__main__":
    unittest.main()

