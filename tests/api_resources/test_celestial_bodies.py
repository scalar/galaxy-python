# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestCelestialBodies:
    @smoke_case("celestialBodies.create:required", operation="create", path="/celestial-bodies")
    def test_method_create(self) -> None:
        celestial_body = client.celestial_bodies.create(
            name="Mars",
        )

    @smoke_case("celestialBodies.create:all", operation="create", path="/celestial-bodies")
    def test_method_create_with_all_params(self) -> None:
        celestial_body = client.celestial_bodies.create(
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
            tags=[""],
            success_callback_url="https://example.com/webhook",
            failure_callback_url="https://example.com/webhook",
        )
