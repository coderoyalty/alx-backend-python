#!/usr/bin/env python3
"""
unittest for utils.py
"""
import unittest
import unittest.mock
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient, get_json
from fixtures import TEST_PAYLOAD


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

    """
    repo={"license": {"key": "my_license"}}, license_key="my_license"
    repo={"license": {"key": "other_license"}}, license_key="my_license"
    """
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, ("my_license"), True),
        ({"license": {"key": "other_license"}}, ("my_license"), False)
    ])
    def test_has_license(self, repo, license, expected):
        """test for has_license"""
        client = GithubOrgClient('test')
        self.assertEqual(client.has_license(repo, license), expected)


@parameterized_class((
    "org_payload", "repos_payload",
    "expected_repos", "apache2_repos"
), TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    client.GithubOrgClient integration test
    """

    @classmethod
    def setUpClass(self):
        """method to create a patch, and mock the `requests.get`"""
        self.get_patcher = patch('requests.get')
        self.mock = self.get_patcher.start()
        self.mock.return_value.json.side_effect = [
            self.org_payload, self.repos_payload,
            self.org_payload, self.repos_payload,
        ]

    @classmethod
    def tearDownClass(self):
        """method to stop the patch"""
        self.get_patcher.stop()

    def test_public_repos(self):
        """
        integration test for public_repos
        """
        client = GithubOrgClient('apple')
        self.assertEqual(client.org, self.org_payload)
        self.assertEqual(client.repos_payload, self.repos_payload)
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """
        integration test for public_repos with license
        """
        client = GithubOrgClient('apple')
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos(
            license="apache-2.0"), self.apache2_repos)
        self.mock.assert_called()
