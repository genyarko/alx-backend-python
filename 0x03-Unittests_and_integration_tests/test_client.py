#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    def test_public_repos_url(self):
        # Mock the 'org' property with a known payload
        with patch.object(GithubOrgClient, 'org', return_value={'repos_url': 'https://api.github.com/orgs/testorg/repos'}):
            client = GithubOrgClient('testorg')
            public_repos_url = client._public_repos_url

        # Check that the result of _public_repos_url is the expected URL based on the mocked payload
        expected_url = 'https://api.github.com/orgs/testorg/repos'
        self.assertEqual(public_repos_url, expected_url)

if __name__ == "__main__":
    unittest.main()
