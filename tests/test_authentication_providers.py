import unittest

import requests_mock

from canvasapi import Canvas
from canvasapi.authentication_providers import AuthenticationProviders
from tests import settings
from tests.util import register_uris


@requests_mock.Mocker()
class TestAuthenticationProviders(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.canvas = Canvas(settings.BASE_URL, settings.API_KEY)

        with requests_mock.Mocker() as m:
            register_uris({
                'account': ['get_by_id', 'add_authentication_providers']
            }, m)

            self.account = self.canvas.get_account(1)
            self.authentication_providers = self.account.add_authentication_providers(
                authentication_providers={
                    "auth_type": "Authentication Providers"
                }
            )

    # update()
    def test_update_authentication_providers(self, m):
        register_uris({'authentication_providers': ['update_authentication_providers']}, m)

        auth_type = 'New Authentication Providers'

        updated_authentication_providers = self.authentication_providers.update(
            authentication_providers={
                "auth_type": auth_type
            }
        )

        self.assertIsInstance(updated_authentication_providers, AuthenticationProviders)
        self.assertTrue(hasattr(updated_authentication_providers, 'auth_type'))
        self.assertEqual(updated_authentication_providers.auth_type, auth_type)

    # delete()
    def test_delete_authentication_providers(self, m):
        register_uris({'authentication_providers': ['delete_authentication_providers']}, m)

        deleted_authentication_providers = self.authentication_providers.delete()

        self.assertIsInstance(deleted_authentication_providers, AuthenticationProviders)
        self.assertTrue(hasattr(deleted_authentication_providers, 'auth_type'))
        self.assertEqual(deleted_authentication_providers.auth_type, 'Authentication Providers')

    # __str__()
    def test_str__(self, m):
        string = str(self.authentication_providers)
        self.assertIsInstance(string, str)
