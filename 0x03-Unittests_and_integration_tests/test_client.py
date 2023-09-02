#!/usr/bin/env python3
"""
unittest for utils.py
"""
import unittest
import unittest.mock
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient, get_json


class TestGithubOrgClient(unittest.TestCase):
    """
    test github org client
    """

    @parameterized.expand([
        ("google"), ("abc")
    ])
    @unittest.mock.patch('client.get_json')
    def test_org(self, org, mock):
        """ test org """
        client = GithubOrgClient(org)
        ORG_URL = GithubOrgClient.ORG_URL
        client.org()
        mock.assert_called_once_with(ORG_URL.format(org=org))

    def test_public_repos_url(self):
        """ unittest _public_repos_url """
        with unittest.mock.patch(
            "client.GithubOrgClient.org",
                new_callable=unittest.mock.PropertyMock) as mock:
            client = GithubOrgClient('apple')
            payload = {"repos_url": "meta"}
            mock.return_value = payload
            res = client._public_repos_url
            self.assertEqual(res, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, get_mock):
        """unittest public_repos"""
        payload = [{"name": "coderoyalty"}]
        get_mock.return_value = payload

        with unittest.mock.patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=unittest.mock.PropertyMock
        ) as prop_mock:
            client = GithubOrgClient('coddies')
            prop_mock.return_value = "code/royalty"
            repos = client.public_repos()
            self.assertEqual(repos, [repo["name"] for repo in payload])
            prop_mock.assert_called_once()
            get_mock.assert_called_once()
