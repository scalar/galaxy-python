# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Optional, Union
from datetime import datetime
from typing_extensions import Literal, overload
from .._types import SequenceNotStr

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
from ..types.celestial_body_create_response import CelestialBodyCreateResponse
from ..types.user_param import UserParam
from ..types import celestial_body_create_params

__all__ = ["CelestialBodiesResource", "AsyncCelestialBodiesResource"]


class CelestialBodiesResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> CelestialBodiesResourceWithRawResponse:
        return CelestialBodiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CelestialBodiesResourceWithStreamingResponse:
        return CelestialBodiesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        type: Literal["terrestrial", "gas_giant", "ice_giant", "dwarf", "super_earth"] | Omit = omit,
        habitability_index: float | Omit = omit,
        physical_properties: celestial_body_create_params.PlanetPhysicalProperties | Omit = omit,
        atmosphere: Iterable[celestial_body_create_params.PlanetAtmosphere] | Omit = omit,
        discovered_at: Union[str, datetime] | Omit = omit,
        image: Optional[str] | Omit = omit,
        satellites: Iterable[celestial_body_create_params.PlanetSatellite] | Omit = omit,
        creator: UserParam | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        success_callback_url: str | Omit = omit,
        failure_callback_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CelestialBodyCreateResponse:
        ...

    @overload
    def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        diameter: float | Omit = omit,
        type: Literal["moon", "asteroid", "comet"] | Omit = omit,
        orbit: celestial_body_create_params.SatelliteOrbit | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CelestialBodyCreateResponse:
        ...

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        type: Union[Literal["terrestrial", "gas_giant", "ice_giant", "dwarf", "super_earth"], Literal["moon", "asteroid", "comet"]] | Omit = omit,
        habitability_index: float | Omit = omit,
        physical_properties: celestial_body_create_params.PlanetPhysicalProperties | Omit = omit,
        atmosphere: Iterable[celestial_body_create_params.PlanetAtmosphere] | Omit = omit,
        discovered_at: Union[str, datetime] | Omit = omit,
        image: Optional[str] | Omit = omit,
        satellites: Iterable[celestial_body_create_params.PlanetSatellite] | Omit = omit,
        creator: UserParam | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        success_callback_url: str | Omit = omit,
        failure_callback_url: str | Omit = omit,
        diameter: float | Omit = omit,
        orbit: celestial_body_create_params.SatelliteOrbit | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CelestialBodyCreateResponse:
        """
        Stars, moons, comets, the occasional rogue asteroid — if it glows or drifts through the void, you can add it here.
        
        Args:
            name: Body parameter.
            description: Body parameter.
            type: Body parameter.
            habitability_index: A score from 0 to 1 indicating potential habitability
            physical_properties: Body parameter.
            atmosphere: Atmospheric composition
            discovered_at: Body parameter.
            image: Body parameter.
            satellites: Body parameter.
            creator: A user
            tags: Body parameter.
            success_callback_url: URL which gets invoked upon a successful operation
            failure_callback_url: URL which gets invoked upon a failed operation
            diameter: Diameter in kilometers
            orbit: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            CelestialBodyCreateResponse: Celestial body created
        
        Example:
            ```python
            celestial_body = client.celestial_bodies.create(
                name="Mars",
            )
            ```
        """
        return self._post(
            "/celestial-bodies",
            body=maybe_transform(
            {
            "name": name,
            "description": description,
            "type": type,
            "habitability_index": habitability_index,
            "physical_properties": physical_properties,
            "atmosphere": atmosphere,
            "discovered_at": discovered_at,
            "image": image,
            "satellites": satellites,
            "creator": creator,
            "tags": tags,
            "success_callback_url": success_callback_url,
            "failure_callback_url": failure_callback_url,
            "diameter": diameter,
            "orbit": orbit,
        },
            celestial_body_create_params.CelestialBodyCreateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CelestialBodyCreateResponse,
        )


class AsyncCelestialBodiesResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncCelestialBodiesResourceWithRawResponse:
        return AsyncCelestialBodiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCelestialBodiesResourceWithStreamingResponse:
        return AsyncCelestialBodiesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        type: Literal["terrestrial", "gas_giant", "ice_giant", "dwarf", "super_earth"] | Omit = omit,
        habitability_index: float | Omit = omit,
        physical_properties: celestial_body_create_params.PlanetPhysicalProperties | Omit = omit,
        atmosphere: Iterable[celestial_body_create_params.PlanetAtmosphere] | Omit = omit,
        discovered_at: Union[str, datetime] | Omit = omit,
        image: Optional[str] | Omit = omit,
        satellites: Iterable[celestial_body_create_params.PlanetSatellite] | Omit = omit,
        creator: UserParam | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        success_callback_url: str | Omit = omit,
        failure_callback_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CelestialBodyCreateResponse:
        ...

    @overload
    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        diameter: float | Omit = omit,
        type: Literal["moon", "asteroid", "comet"] | Omit = omit,
        orbit: celestial_body_create_params.SatelliteOrbit | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CelestialBodyCreateResponse:
        ...

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        type: Union[Literal["terrestrial", "gas_giant", "ice_giant", "dwarf", "super_earth"], Literal["moon", "asteroid", "comet"]] | Omit = omit,
        habitability_index: float | Omit = omit,
        physical_properties: celestial_body_create_params.PlanetPhysicalProperties | Omit = omit,
        atmosphere: Iterable[celestial_body_create_params.PlanetAtmosphere] | Omit = omit,
        discovered_at: Union[str, datetime] | Omit = omit,
        image: Optional[str] | Omit = omit,
        satellites: Iterable[celestial_body_create_params.PlanetSatellite] | Omit = omit,
        creator: UserParam | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        success_callback_url: str | Omit = omit,
        failure_callback_url: str | Omit = omit,
        diameter: float | Omit = omit,
        orbit: celestial_body_create_params.SatelliteOrbit | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CelestialBodyCreateResponse:
        """
        Stars, moons, comets, the occasional rogue asteroid — if it glows or drifts through the void, you can add it here.
        
        Args:
            name: Body parameter.
            description: Body parameter.
            type: Body parameter.
            habitability_index: A score from 0 to 1 indicating potential habitability
            physical_properties: Body parameter.
            atmosphere: Atmospheric composition
            discovered_at: Body parameter.
            image: Body parameter.
            satellites: Body parameter.
            creator: A user
            tags: Body parameter.
            success_callback_url: URL which gets invoked upon a successful operation
            failure_callback_url: URL which gets invoked upon a failed operation
            diameter: Diameter in kilometers
            orbit: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            CelestialBodyCreateResponse: Celestial body created
        
        Example:
            ```python
            celestial_body = await client.celestial_bodies.create(
                name="Mars",
            )
            ```
        """
        return await self._post(
            "/celestial-bodies",
            body=await async_maybe_transform(
            {
            "name": name,
            "description": description,
            "type": type,
            "habitability_index": habitability_index,
            "physical_properties": physical_properties,
            "atmosphere": atmosphere,
            "discovered_at": discovered_at,
            "image": image,
            "satellites": satellites,
            "creator": creator,
            "tags": tags,
            "success_callback_url": success_callback_url,
            "failure_callback_url": failure_callback_url,
            "diameter": diameter,
            "orbit": orbit,
        },
            celestial_body_create_params.CelestialBodyCreateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CelestialBodyCreateResponse,
        )


class CelestialBodiesResourceWithRawResponse:
    def __init__(self, celestial_bodies: CelestialBodiesResource) -> None:
        self._celestial_bodies = celestial_bodies

        self.create = to_raw_response_wrapper(
            celestial_bodies.create,
        )


class AsyncCelestialBodiesResourceWithRawResponse:
    def __init__(self, celestial_bodies: AsyncCelestialBodiesResource) -> None:
        self._celestial_bodies = celestial_bodies

        self.create = async_to_raw_response_wrapper(
            celestial_bodies.create,
        )


class CelestialBodiesResourceWithStreamingResponse:
    def __init__(self, celestial_bodies: CelestialBodiesResource) -> None:
        self._celestial_bodies = celestial_bodies

        self.create = to_streamed_response_wrapper(
            celestial_bodies.create,
        )


class AsyncCelestialBodiesResourceWithStreamingResponse:
    def __init__(self, celestial_bodies: AsyncCelestialBodiesResource) -> None:
        self._celestial_bodies = celestial_bodies

        self.create = async_to_streamed_response_wrapper(
            celestial_bodies.create,
        )
