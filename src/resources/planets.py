# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Mapping, Optional, Union, cast
from datetime import datetime
from typing_extensions import Literal
from .._types import FileTypes, SequenceNotStr

from .._types import Body, Omit, Query, Headers, NotGiven, NoneType, omit, not_given
from .._files import deepcopy_with_paths
from .._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.planet_list_all_data_response import PlanetListAllDataResponse
from ..types import planet_list_all_data_params, planet_create_params, planet_update_params, planet_upload_image_params
from ..types.planet import Planet
from ..types.user_param import UserParam
from ..types.planet_upload_image_response import PlanetUploadImageResponse

__all__ = ["PlanetsResource", "AsyncPlanetsResource"]


class PlanetsResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> PlanetsResourceWithRawResponse:
        return PlanetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlanetsResourceWithStreamingResponse:
        return PlanetsResourceWithStreamingResponse(self)

    def list_all_data(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanetListAllDataResponse:
        """
        It's easy to say you know them all, but do you really? Retrieve all the planets and check whether you missed one.
        
        Args:
            limit: The number of items to return
            offset: The number of items to skip before starting to collect the result set
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            PlanetListAllDataResponse: OK
        
        Example:
            ```python
            planet = client.planets.list_all_data(
                limit=10,
                offset=0,
            )
            ```
        """
        return self._get(
            "/planets",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"limit": limit, "offset": offset}, planet_list_all_data_params.PlanetListAllDataParams)),
            cast_to=PlanetListAllDataResponse,
        )

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        type: Literal["terrestrial", "gas_giant", "ice_giant", "dwarf", "super_earth"] | Omit = omit,
        habitability_index: float | Omit = omit,
        physical_properties: planet_create_params.PhysicalProperties | Omit = omit,
        atmosphere: Iterable[planet_create_params.Atmosphere] | Omit = omit,
        discovered_at: Union[str, datetime] | Omit = omit,
        image: Optional[str] | Omit = omit,
        satellites: Iterable[planet_create_params.Satellite] | Omit = omit,
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
    ) -> Planet:
        """
        Time to play god and create a new planet. What do you think? Ah, don't think too much. What could go wrong anyway?
        
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
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            Planet: Created
        
        Example:
            ```python
            planet = client.planets.create(
                name="Mars",
            )
            ```
        """
        return self._post(
            "/planets",
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
        },
            planet_create_params.PlanetCreateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Planet,
        )

    def retrieve(
        self,
        planet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Planet:
        """
        You'll better learn a little bit more about the planets. It might come in handy once space travel is available for everyone.
        
        Args:
            planet_id: The ID of the planet to get
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            Planet: Planet Found
        
        Example:
            ```python
            planet = client.planets.retrieve(
                planet_id=1,
            )
            ```
        """
        if planet_id is None or (isinstance(planet_id, str) and not planet_id):
            raise ValueError(f"Expected a non-empty value for `planet_id` but received {planet_id!r}")
        return self._get(
            path_template("/planets/{planetId}", **{"planetId": planet_id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Planet,
        )

    def update(
        self,
        planet_id: int,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        type: Literal["terrestrial", "gas_giant", "ice_giant", "dwarf", "super_earth"] | Omit = omit,
        habitability_index: float | Omit = omit,
        physical_properties: planet_update_params.PhysicalProperties | Omit = omit,
        atmosphere: Iterable[planet_update_params.Atmosphere] | Omit = omit,
        discovered_at: Union[str, datetime] | Omit = omit,
        image: Optional[str] | Omit = omit,
        satellites: Iterable[planet_update_params.Satellite] | Omit = omit,
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
    ) -> Planet:
        """
        Sometimes you make mistakes, that's fine. No worries, you can update all planets.
        
        Args:
            planet_id: The ID of the planet to get
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
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            Planet: Planet updated successfully
        
        Example:
            ```python
            planet = client.planets.update(
                planet_id=1,
                name="Mars",
            )
            ```
        """
        if planet_id is None or (isinstance(planet_id, str) and not planet_id):
            raise ValueError(f"Expected a non-empty value for `planet_id` but received {planet_id!r}")
        return self._put(
            path_template("/planets/{planetId}", **{"planetId": planet_id}),
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
        },
            planet_update_params.PlanetUpdateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Planet,
        )

    def delete(
        self,
        planet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        This endpoint was used to delete planets. Unfortunately, that caused a lot of trouble for planets with life. So, this endpoint is now deprecated and should not be used anymore.
        
        Args:
            planet_id: The ID of the planet to get
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            No Content
        
        Example:
            ```python
            client.planets.delete(
                planet_id=1,
            )
            ```
        """
        if planet_id is None or (isinstance(planet_id, str) and not planet_id):
            raise ValueError(f"Expected a non-empty value for `planet_id` but received {planet_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/planets/{planetId}", **{"planetId": planet_id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def upload_image(
        self,
        planet_id: int,
        *,
        image: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanetUploadImageResponse:
        """
        Got a crazy good photo of a planet? Share it with the world!
        
        Args:
            planet_id: The ID of the planet to get
            image: The image file to upload
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            PlanetUploadImageResponse: Image uploaded
        
        Example:
            ```python
            planet = client.planets.upload_image(
                planet_id=1,
            )
            ```
        """
        if planet_id is None or (isinstance(planet_id, str) and not planet_id):
            raise ValueError(f"Expected a non-empty value for `planet_id` but received {planet_id!r}")
        body = deepcopy_with_paths(
            {
                "image": image,
            },
            [["image"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["image"]])
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/planets/{planetId}/image", **{"planetId": planet_id}),
            body=maybe_transform(body, planet_upload_image_params.PlanetUploadImageParams),
            files=files,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PlanetUploadImageResponse,
        )


class AsyncPlanetsResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncPlanetsResourceWithRawResponse:
        return AsyncPlanetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlanetsResourceWithStreamingResponse:
        return AsyncPlanetsResourceWithStreamingResponse(self)

    async def list_all_data(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanetListAllDataResponse:
        """
        It's easy to say you know them all, but do you really? Retrieve all the planets and check whether you missed one.
        
        Args:
            limit: The number of items to return
            offset: The number of items to skip before starting to collect the result set
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            PlanetListAllDataResponse: OK
        
        Example:
            ```python
            planet = await client.planets.list_all_data(
                limit=10,
                offset=0,
            )
            ```
        """
        return await self._get(
            "/planets",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"limit": limit, "offset": offset}, planet_list_all_data_params.PlanetListAllDataParams)),
            cast_to=PlanetListAllDataResponse,
        )

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        type: Literal["terrestrial", "gas_giant", "ice_giant", "dwarf", "super_earth"] | Omit = omit,
        habitability_index: float | Omit = omit,
        physical_properties: planet_create_params.PhysicalProperties | Omit = omit,
        atmosphere: Iterable[planet_create_params.Atmosphere] | Omit = omit,
        discovered_at: Union[str, datetime] | Omit = omit,
        image: Optional[str] | Omit = omit,
        satellites: Iterable[planet_create_params.Satellite] | Omit = omit,
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
    ) -> Planet:
        """
        Time to play god and create a new planet. What do you think? Ah, don't think too much. What could go wrong anyway?
        
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
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            Planet: Created
        
        Example:
            ```python
            planet = await client.planets.create(
                name="Mars",
            )
            ```
        """
        return await self._post(
            "/planets",
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
        },
            planet_create_params.PlanetCreateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Planet,
        )

    async def retrieve(
        self,
        planet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Planet:
        """
        You'll better learn a little bit more about the planets. It might come in handy once space travel is available for everyone.
        
        Args:
            planet_id: The ID of the planet to get
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            Planet: Planet Found
        
        Example:
            ```python
            planet = await client.planets.retrieve(
                planet_id=1,
            )
            ```
        """
        if planet_id is None or (isinstance(planet_id, str) and not planet_id):
            raise ValueError(f"Expected a non-empty value for `planet_id` but received {planet_id!r}")
        return await self._get(
            path_template("/planets/{planetId}", **{"planetId": planet_id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Planet,
        )

    async def update(
        self,
        planet_id: int,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        type: Literal["terrestrial", "gas_giant", "ice_giant", "dwarf", "super_earth"] | Omit = omit,
        habitability_index: float | Omit = omit,
        physical_properties: planet_update_params.PhysicalProperties | Omit = omit,
        atmosphere: Iterable[planet_update_params.Atmosphere] | Omit = omit,
        discovered_at: Union[str, datetime] | Omit = omit,
        image: Optional[str] | Omit = omit,
        satellites: Iterable[planet_update_params.Satellite] | Omit = omit,
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
    ) -> Planet:
        """
        Sometimes you make mistakes, that's fine. No worries, you can update all planets.
        
        Args:
            planet_id: The ID of the planet to get
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
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            Planet: Planet updated successfully
        
        Example:
            ```python
            planet = await client.planets.update(
                planet_id=1,
                name="Mars",
            )
            ```
        """
        if planet_id is None or (isinstance(planet_id, str) and not planet_id):
            raise ValueError(f"Expected a non-empty value for `planet_id` but received {planet_id!r}")
        return await self._put(
            path_template("/planets/{planetId}", **{"planetId": planet_id}),
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
        },
            planet_update_params.PlanetUpdateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Planet,
        )

    async def delete(
        self,
        planet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        This endpoint was used to delete planets. Unfortunately, that caused a lot of trouble for planets with life. So, this endpoint is now deprecated and should not be used anymore.
        
        Args:
            planet_id: The ID of the planet to get
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            No Content
        
        Example:
            ```python
            await client.planets.delete(
                planet_id=1,
            )
            ```
        """
        if planet_id is None or (isinstance(planet_id, str) and not planet_id):
            raise ValueError(f"Expected a non-empty value for `planet_id` but received {planet_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/planets/{planetId}", **{"planetId": planet_id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def upload_image(
        self,
        planet_id: int,
        *,
        image: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanetUploadImageResponse:
        """
        Got a crazy good photo of a planet? Share it with the world!
        
        Args:
            planet_id: The ID of the planet to get
            image: The image file to upload
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            PlanetUploadImageResponse: Image uploaded
        
        Example:
            ```python
            planet = await client.planets.upload_image(
                planet_id=1,
            )
            ```
        """
        if planet_id is None or (isinstance(planet_id, str) and not planet_id):
            raise ValueError(f"Expected a non-empty value for `planet_id` but received {planet_id!r}")
        body = deepcopy_with_paths(
            {
                "image": image,
            },
            [["image"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["image"]])
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/planets/{planetId}/image", **{"planetId": planet_id}),
            body=await async_maybe_transform(body, planet_upload_image_params.PlanetUploadImageParams),
            files=files,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PlanetUploadImageResponse,
        )


class PlanetsResourceWithRawResponse:
    def __init__(self, planets: PlanetsResource) -> None:
        self._planets = planets

        self.list_all_data = to_raw_response_wrapper(
            planets.list_all_data,
        )
        self.create = to_raw_response_wrapper(
            planets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            planets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            planets.update,
        )
        self.delete = to_raw_response_wrapper(
            planets.delete,
        )
        self.upload_image = to_raw_response_wrapper(
            planets.upload_image,
        )


class AsyncPlanetsResourceWithRawResponse:
    def __init__(self, planets: AsyncPlanetsResource) -> None:
        self._planets = planets

        self.list_all_data = async_to_raw_response_wrapper(
            planets.list_all_data,
        )
        self.create = async_to_raw_response_wrapper(
            planets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            planets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            planets.update,
        )
        self.delete = async_to_raw_response_wrapper(
            planets.delete,
        )
        self.upload_image = async_to_raw_response_wrapper(
            planets.upload_image,
        )


class PlanetsResourceWithStreamingResponse:
    def __init__(self, planets: PlanetsResource) -> None:
        self._planets = planets

        self.list_all_data = to_streamed_response_wrapper(
            planets.list_all_data,
        )
        self.create = to_streamed_response_wrapper(
            planets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            planets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            planets.update,
        )
        self.delete = to_streamed_response_wrapper(
            planets.delete,
        )
        self.upload_image = to_streamed_response_wrapper(
            planets.upload_image,
        )


class AsyncPlanetsResourceWithStreamingResponse:
    def __init__(self, planets: AsyncPlanetsResource) -> None:
        self._planets = planets

        self.list_all_data = async_to_streamed_response_wrapper(
            planets.list_all_data,
        )
        self.create = async_to_streamed_response_wrapper(
            planets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            planets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            planets.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            planets.delete,
        )
        self.upload_image = async_to_streamed_response_wrapper(
            planets.upload_image,
        )
