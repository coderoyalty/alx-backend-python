#!/usr/bin/env python3
"""
unittest for utils.py
"""
import unittest
import unittest.mock
from parameterized import parameterized
from client import GithubOrgClient


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
