# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke test: calls every generated operation once to confirm the SDK can reach each endpoint.
# Run it from this repo with `python tests/smoke-test.py`. The generator also runs this file
# against a mock server and reads the JSON report produced via SCALAR_SMOKE_REPORT.
from __future__ import annotations

import json
import os
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, TypedDict

from scalar_galaxy import Galaxy

# The shared smoke-test runner injects base URL and credentials through the same
# environment variables the generated client reads in normal use.
client = Galaxy(max_retries=0, timeout=30)


class SmokeResult(TypedDict, total=False):
    operation: str
    method: str
    path: str
    label: str
    status: str
    durationMs: int
    error: str


class _SmokeCaseBase(TypedDict):
    operation: str
    method: str
    path: str
    run: Callable[[], Any]


# `label` says which of an operation's two calls this is — "required params" or "all params".
# It sits in a total=False extension because it is absent when the operation contributed a
# single case, while the fields above are always present.
class SmokeCase(_SmokeCaseBase, total=False):
    label: str


def _smoke_case_0() -> None:
    planet = client.planets.list_all_data(
        limit=10,
        offset=0,
    )


def _smoke_case_1() -> None:
    planet = client.planets.create(
        name="Mars",
    )


def _smoke_case_2() -> None:
    planet = client.planets.create(
        name="Mars",
        description="The red planet",
        type="terrestrial",
        habitability_index=0.68,
        physical_properties={"mass": 0.107, "radius": 0.532, "gravity": 0.378, "temperature": {}},
        atmosphere=[],
        discovered_at="1610-01-07T00:00:00Z",
        image="https://cdn.scalar.com/photos/mars.jpg",
        satellites=[],
        creator={"name": "Marc"},
        tags=[],
        success_callback_url="https://example.com/webhook",
        failure_callback_url="https://example.com/webhook",
    )


def _smoke_case_3() -> None:
    planet = client.planets.retrieve(
        planet_id=1,
    )


def _smoke_case_4() -> None:
    planet = client.planets.update(
        planet_id=1,
        name="Mars",
    )


def _smoke_case_5() -> None:
    planet = client.planets.update(
        planet_id=1,
        name="Mars",
        description="The red planet",
        type="terrestrial",
        habitability_index=0.68,
        physical_properties={"mass": 0.107, "radius": 0.532, "gravity": 0.378, "temperature": {}},
        atmosphere=[],
        discovered_at="1610-01-07T00:00:00Z",
        image="https://cdn.scalar.com/photos/mars.jpg",
        satellites=[],
        creator={"name": "Marc"},
        tags=[],
        success_callback_url="https://example.com/webhook",
        failure_callback_url="https://example.com/webhook",
    )


def _smoke_case_6() -> None:
    client.planets.delete(
        planet_id=1,
    )


def _smoke_case_7() -> None:
    planet = client.planets.delte_image(
        planet_id=1,
    )


def _smoke_case_8() -> None:
    planet = client.planets.delte_image(
        planet_id=1,
        image=b"@mars.jpg",
    )


def _smoke_case_9() -> None:
    celestial_body = client.celestial_bodies.create(
        name="Mars",
    )


def _smoke_case_10() -> None:
    celestial_body = client.celestial_bodies.create(
        name="Mars",
        description="The red planet",
        type="terrestrial",
        habitability_index=0.68,
        physical_properties={"mass": 0.107, "radius": 0.532, "gravity": 0.378, "temperature": {}},
        atmosphere=[],
        discovered_at="1610-01-07T00:00:00Z",
        image="https://cdn.scalar.com/photos/mars.jpg",
        satellites=[],
        creator={"name": "Marc"},
        tags=[],
        success_callback_url="https://example.com/webhook",
        failure_callback_url="https://example.com/webhook",
    )


def _smoke_case_11() -> None:
    authentication = client.authentication.create_user(
        name="Marc",
        email="marc@scalar.com",
        password="i-love-scalar",
    )


def _smoke_case_12() -> None:
    authentication = client.authentication.create_token(
        email="marc@scalar.com",
        password="i-love-scalar",
    )


def _smoke_case_13() -> None:
    authentication = client.authentication.list_me()


cases: list[SmokeCase] = [
    {
        "operation": "listAllData",
        "method": "GET",
        "path": "/planets",
        "run": _smoke_case_0,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/planets",
        "label": "required params",
        "run": _smoke_case_1,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/planets",
        "label": "all params",
        "run": _smoke_case_2,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/planets/{planetId}",
        "run": _smoke_case_3,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/planets/{planetId}",
        "label": "required params",
        "run": _smoke_case_4,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/planets/{planetId}",
        "label": "all params",
        "run": _smoke_case_5,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/planets/{planetId}",
        "run": _smoke_case_6,
    },
    {
        "operation": "delteImage",
        "method": "POST",
        "path": "/planets/{planetId}/image",
        "label": "required params",
        "run": _smoke_case_7,
    },
    {
        "operation": "delteImage",
        "method": "POST",
        "path": "/planets/{planetId}/image",
        "label": "all params",
        "run": _smoke_case_8,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/celestial-bodies",
        "label": "required params",
        "run": _smoke_case_9,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/celestial-bodies",
        "label": "all params",
        "run": _smoke_case_10,
    },
    {
        "operation": "createUser",
        "method": "POST",
        "path": "/user/signup",
        "run": _smoke_case_11,
    },
    {
        "operation": "createToken",
        "method": "POST",
        "path": "/auth/token",
        "run": _smoke_case_12,
    },
    {
        "operation": "listMe",
        "method": "GET",
        "path": "/me",
        "run": _smoke_case_13,
    },
]

DEFAULT_SMOKE_CONCURRENCY = 32


def _selected_cases() -> list[SmokeCase]:
    filter_value = os.environ.get("SCALAR_SMOKE_FILTER")
    needles = [needle.strip() for needle in filter_value.split(",") if needle.strip()] if filter_value else []
    if not needles:
        return cases
    return [case for case in cases if any(needle in case["operation"] or needle in case["path"] for needle in needles)]


def _smoke_concurrency(case_count: int) -> int:
    override = os.environ.get("SCALAR_SMOKE_CONCURRENCY")
    if override:
        try:
            parsed = int(override)
            if parsed > 0:
                return min(parsed, case_count)
        except ValueError:
            pass
    return min(DEFAULT_SMOKE_CONCURRENCY, case_count)


def _case_identity(case: SmokeCase) -> SmokeResult:
    # `label` is carried through only when the operation contributed both of its calls, so a
    # single-case operation reports exactly as it did before there were two.
    identity: SmokeResult = {
        "operation": case["operation"],
        "method": case["method"],
        "path": case["path"],
    }
    label = case.get("label")
    if label:
        identity["label"] = label
    return identity


def _run_case(case: SmokeCase) -> SmokeResult:
    started_at = time.monotonic()
    identity = _case_identity(case)
    try:
        case["run"]()
        return {
            **identity,
            "status": "passed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
        }
    except Exception:
        return {
            **identity,
            "status": "failed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
            "error": traceback.format_exc(),
        }


def main() -> None:
    selected = _selected_cases()
    if selected:
        # Keep enough parallelism to catch generated SDK concurrency bugs without overwhelming
        # CI runners or the in-process mock server for large SDKs.
        with ThreadPoolExecutor(max_workers=_smoke_concurrency(len(selected))) as executor:
            results = list(executor.map(_run_case, selected))
    else:
        results = []
    failed = [result for result in results if result["status"] == "failed"]

    report_path = os.environ.get("SCALAR_SMOKE_REPORT")
    if report_path:
        Path(report_path).write_text(
            json.dumps({"total": len(results), "failed": len(failed), "results": results}), encoding="utf-8"
        )
    else:
        for result in results:
            suffix = f" [{result['label']}]" if result.get("label") else ""
            if result["status"] == "passed":
                print(
                    f"PASS {result['operation']}{suffix} ({result['method']} {result['path']}) {result['durationMs']}ms"
                )
            else:
                print(
                    f"FAIL {result['operation']}{suffix} ({result['method']} {result['path']})\n{result.get('error', '')}",
                    file=sys.stderr,
                )
        if not results:
            print("No code samples ran (empty SDK or a SCALAR_SMOKE_FILTER that matched nothing).", file=sys.stderr)
        else:
            print(f"\n{len(results) - len(failed)}/{len(results)} samples passed")

    if failed or not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
