#!/usr/bin/env python3
""" Defines the TestGithubOrgClient class """

import unittest
from unittest.mock import Mock, MagicMock, PropertyMock, patch
from typing import Dict
import client
import fixtures
from parameterized import parameterized, parameterized_class
from requests import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """
        Provides functionality for testing that GithubOrgClient class
        returns the expected result
    """

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"})
    ])
    @patch("client.get_json")
    def test_org(self,
                 org: str,
                 response: Dict,
                 mocked_fn: MagicMock
                 ) -> None:
        """ Tests that GithubOrgClient returns the expected result """
        mocked_fn.return_value = MagicMock(return_value=response)
        git_client = client.GithubOrgClient(org)
        self.assertEqual(git_client.org(), response)
        mocked_fn.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org)
                )

    def test_public_repos_url(self) -> None:
        """ Tests that _public_repos_url produces expected result """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_payload:
            mock_payload.return_value = {
                'repos_url': "https://api.github.com/users/google/repos"
            }
            self.assertEqual(
                client.GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """ Tests that public_repos prodcues expected result """
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mocked_public_repos:
            mocked_public_repos.return_value = test_payload["repos_url"]
            self.assertEqual(
                client.GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mocked_public_repos.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self,
                         repo: Dict,
                         key: str,
                         expected: bool
                         ) -> None:
        """ Tests that has_license produces expected result """
        client_org = client.GithubOrgClient("google")
        client_licence = client_org.has_license(repo, key)
        self.assertEqual(client_licence, expected)


@parameterized_class([
    {
        'org_payload': fixtures.TEST_PAYLOAD[0][0],
        'repos_payload': fixtures.TEST_PAYLOAD[0][1],
        'expected_repos': fixtures.TEST_PAYLOAD[0][2],
        'apache2_repos': fixtures.TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
        Provides fumctionality to perform integration tests on
        GithubOrgClient class
    """
    @classmethod
    def setUpClass(cls) -> None:
        """ Sets up initial class fixtures """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """ Tests that public_repos returns expected result """
        self.assertEqual(
            client.GithubOrgClient("google").public_repos(),
            self.expected_repos
        )

    def test_public_repos_with_license(self) -> None:
        """ Tests that public_repos with license returns expected o/p """
        self.assertEqual(
            client.GithubOrgClient("google")
            .public_repos(license="apache-2.0"),
            self.apache2_repos
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """ Tears down the initial class fixtures """
        cls.get_patcher.stop()
