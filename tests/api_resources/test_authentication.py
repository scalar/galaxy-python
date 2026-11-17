# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestAuthentication:
    @smoke_case("authentication.createUser:single", operation="createUser", path="/user/signup")
    def test_method_create_user(self) -> None:
        authentication = client.authentication.create_user(
            name="Marc",
            email="marc@scalar.com",
            password="i-love-scalar",
        )

    @smoke_case("authentication.createToken:single", operation="createToken", path="/auth/token")
    def test_method_create_token(self) -> None:
        authentication = client.authentication.create_token(
            email="marc@scalar.com",
            password="i-love-scalar",
        )

    @smoke_case("authentication.listMe:single", operation="listMe", path="/me")
    def test_method_list_me(self) -> None:
        authentication = client.authentication.list_me()
