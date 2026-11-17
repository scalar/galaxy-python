# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestPlanets:
    @smoke_case("planets.list:single", operation="list", path="/planets")
    def test_method_list(self) -> None:
        planet = client.planets.list(
            limit=10,
            offset=0,
        )

    @smoke_case("planets.create:required", operation="create", path="/planets")
    def test_method_create(self) -> None:
        planet = client.planets.create(
            name="Mars",
        )

    @smoke_case("planets.create:all", operation="create", path="/planets")
    def test_method_create_with_all_params(self) -> None:
        planet = client.planets.create(
            name="Mars",
            description="The red planet",
            type="terrestrial",
            habitability_index=0.68,
            physical_properties={"mass": 0.107, "radius": 0.532, "gravity": 0.378, "temperature": {}},
            atmosphere=[{}],
            discovered_at="1610-01-07T00:00:00Z",
            image="https://cdn.scalar.com/photos/mars.jpg",
            satellites=[{"name": "Phobos"}],
            creator={"name": "Marc"},
            tags=["solar-system", "rocky", "explored"],
            success_callback_url="https://example.com/webhook",
            failure_callback_url="https://example.com/webhook",
        )

    @smoke_case("planets.retrieve:single", operation="retrieve", path="/planets/{planetId}")
    def test_method_retrieve(self) -> None:
        planet = client.planets.retrieve(
            planet_id=1,
        )

    @smoke_case("planets.update:required", operation="update", path="/planets/{planetId}")
    def test_method_update(self) -> None:
        planet = client.planets.update(
            planet_id=1,
            name="Mars",
        )

    @smoke_case("planets.update:all", operation="update", path="/planets/{planetId}")
    def test_method_update_with_all_params(self) -> None:
        planet = client.planets.update(
            planet_id=1,
            name="Mars",
            description="The red planet",
            type="terrestrial",
            habitability_index=0.68,
            physical_properties={"mass": 0.107, "radius": 0.532, "gravity": 0.378, "temperature": {}},
            atmosphere=[{}],
            discovered_at="1610-01-07T00:00:00Z",
            image="https://cdn.scalar.com/photos/mars.jpg",
            satellites=[{"name": "Phobos"}],
            creator={"name": "Marc"},
            tags=["solar-system", "rocky", "explored"],
            success_callback_url="https://example.com/webhook",
            failure_callback_url="https://example.com/webhook",
        )

    @smoke_case("planets.delete:single", operation="delete", path="/planets/{planetId}")
    def test_method_delete(self) -> None:
        client.planets.delete(
            planet_id=1,
        )

    @smoke_case("planets.uploadImage:required", operation="uploadImage", path="/planets/{planetId}/image")
    def test_method_upload_image(self) -> None:
        planet = client.planets.upload_image(
            planet_id=1,
        )

    @smoke_case("planets.uploadImage:all", operation="uploadImage", path="/planets/{planetId}/image")
    def test_method_upload_image_with_all_params(self) -> None:
        planet = client.planets.upload_image(
            planet_id=1,
            image=b"@mars.jpg",
        )
