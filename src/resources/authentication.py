# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.user import User
from ..types import authentication_create_user_params, authentication_create_token_params
from ..types.authentication_create_token_response import AuthenticationCreateTokenResponse

__all__ = ["AuthenticationResource", "AsyncAuthenticationResource"]


class AuthenticationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthenticationResourceWithRawResponse:
        return AuthenticationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticationResourceWithStreamingResponse:
        return AuthenticationResourceWithStreamingResponse(self)

    def create_user(
        self,
        *,
        name: str | Omit = omit,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Time to create a user account, eh?

        Args:
            name: Body parameter.
            email: Body parameter.
            password: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            User: User account created successfully

        Example:
            ```python
            authentication = client.authentication.create_user(
                name="Marc",
                email="marc@scalar.com",
                password="i-love-scalar",
            )
            ```
        """
        return self._post(
            "/user/signup",
            body=maybe_transform(
                {
                    "name": name,
                    "email": email,
                    "password": password,
                },
                authentication_create_user_params.AuthenticationCreateUserParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def create_token(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticationCreateTokenResponse:
        """
        Yeah, this is the boring security stuff. Just get your super secret token and move on.

        Args:
            email: Body parameter.
            password: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AuthenticationCreateTokenResponse: Token Created

        Example:
            ```python
            authentication = client.authentication.create_token(
                email="marc@scalar.com",
                password="i-love-scalar",
            )
            ```
        """
        return self._post(
            "/auth/token",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                authentication_create_token_params.AuthenticationCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationCreateTokenResponse,
        )

    def list_me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Find yourself they say. That's what you can do here.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            User: Authenticated user information retrieved successfully

        Example:
            ```python
            authentication = client.authentication.list_me()
            ```
        """
        return self._get(
            "/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class AsyncAuthenticationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthenticationResourceWithRawResponse:
        return AsyncAuthenticationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticationResourceWithStreamingResponse:
        return AsyncAuthenticationResourceWithStreamingResponse(self)

    async def create_user(
        self,
        *,
        name: str | Omit = omit,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Time to create a user account, eh?

        Args:
            name: Body parameter.
            email: Body parameter.
            password: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            User: User account created successfully

        Example:
            ```python
            authentication = await client.authentication.create_user(
                name="Marc",
                email="marc@scalar.com",
                password="i-love-scalar",
            )
            ```
        """
        return await self._post(
            "/user/signup",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "email": email,
                    "password": password,
                },
                authentication_create_user_params.AuthenticationCreateUserParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def create_token(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticationCreateTokenResponse:
        """
        Yeah, this is the boring security stuff. Just get your super secret token and move on.

        Args:
            email: Body parameter.
            password: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AuthenticationCreateTokenResponse: Token Created

        Example:
            ```python
            authentication = await client.authentication.create_token(
                email="marc@scalar.com",
                password="i-love-scalar",
            )
            ```
        """
        return await self._post(
            "/auth/token",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                authentication_create_token_params.AuthenticationCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationCreateTokenResponse,
        )

    async def list_me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Find yourself they say. That's what you can do here.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            User: Authenticated user information retrieved successfully

        Example:
            ```python
            authentication = await client.authentication.list_me()
            ```
        """
        return await self._get(
            "/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class AuthenticationResourceWithRawResponse:
    def __init__(self, authentication: AuthenticationResource) -> None:
        self._authentication = authentication

        self.create_user = to_raw_response_wrapper(
            authentication.create_user,
        )
        self.create_token = to_raw_response_wrapper(
            authentication.create_token,
        )
        self.list_me = to_raw_response_wrapper(
            authentication.list_me,
        )


class AsyncAuthenticationResourceWithRawResponse:
    def __init__(self, authentication: AsyncAuthenticationResource) -> None:
        self._authentication = authentication

        self.create_user = async_to_raw_response_wrapper(
            authentication.create_user,
        )
        self.create_token = async_to_raw_response_wrapper(
            authentication.create_token,
        )
        self.list_me = async_to_raw_response_wrapper(
            authentication.list_me,
        )


class AuthenticationResourceWithStreamingResponse:
    def __init__(self, authentication: AuthenticationResource) -> None:
        self._authentication = authentication

        self.create_user = to_streamed_response_wrapper(
            authentication.create_user,
        )
        self.create_token = to_streamed_response_wrapper(
            authentication.create_token,
        )
        self.list_me = to_streamed_response_wrapper(
            authentication.list_me,
        )


class AsyncAuthenticationResourceWithStreamingResponse:
    def __init__(self, authentication: AsyncAuthenticationResource) -> None:
        self._authentication = authentication

        self.create_user = async_to_streamed_response_wrapper(
            authentication.create_user,
        )
        self.create_token = async_to_streamed_response_wrapper(
            authentication.create_token,
        )
        self.list_me = async_to_streamed_response_wrapper(
            authentication.list_me,
        )
