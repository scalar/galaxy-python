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
    status: str
    durationMs: int
    error: str


class SmokeCase(TypedDict):
    operation: str
    method: str
    path: str
    run: Callable[[], Any]


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
    planet = client.planets.retrieve(
        planet_id=1,
    )

def _smoke_case_3() -> None:
    planet = client.planets.update(
        planet_id=1,
        name="Mars",
    )

def _smoke_case_4() -> None:
    client.planets.delete(
        planet_id=1,
    )

def _smoke_case_5() -> None:
    planet = client.planets.upload_image(
        planet_id=1,
    )

def _smoke_case_6() -> None:
    celestial_body = client.celestial_bodies.create(
        name="Mars",
    )

def _smoke_case_7() -> None:
    authentication = client.authentication.create_user(
        name="Marc",
        email="marc@scalar.com",
        password="i-love-scalar",
    )

def _smoke_case_8() -> None:
    authentication = client.authentication.create_token(
        email="marc@scalar.com",
        password="i-love-scalar",
    )

def _smoke_case_9() -> None:
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
        "run": _smoke_case_1,
    },

    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/planets/{planetId}",
        "run": _smoke_case_2,
    },

    {
        "operation": "update",
        "method": "PUT",
        "path": "/planets/{planetId}",
        "run": _smoke_case_3,
    },

    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/planets/{planetId}",
        "run": _smoke_case_4,
    },

    {
        "operation": "uploadImage",
        "method": "POST",
        "path": "/planets/{planetId}/image",
        "run": _smoke_case_5,
    },

    {
        "operation": "create",
        "method": "POST",
        "path": "/celestial-bodies",
        "run": _smoke_case_6,
    },

    {
        "operation": "createUser",
        "method": "POST",
        "path": "/user/signup",
        "run": _smoke_case_7,
    },

    {
        "operation": "createToken",
        "method": "POST",
        "path": "/auth/token",
        "run": _smoke_case_8,
    },

    {
        "operation": "listMe",
        "method": "GET",
        "path": "/me",
        "run": _smoke_case_9,
    },

]

DEFAULT_SMOKE_CONCURRENCY = 32


def _selected_cases() -> list[SmokeCase]:
    filter_value = os.environ.get("SCALAR_SMOKE_FILTER")
    needles = [needle.strip() for needle in filter_value.split(",") if needle.strip()] if filter_value else []
    if not needles:
        return cases
    return [
        case
        for case in cases
        if any(needle in case["operation"] or needle in case["path"] for needle in needles)
    ]


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


def _run_case(case: SmokeCase) -> SmokeResult:
    started_at = time.monotonic()
    try:
        case["run"]()
        return {
            "operation": case["operation"],
            "method": case["method"],
            "path": case["path"],
            "status": "passed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
        }
    except Exception:
        return {
            "operation": case["operation"],
            "method": case["method"],
            "path": case["path"],
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
        Path(report_path).write_text(json.dumps({"total": len(results), "failed": len(failed), "results": results}), encoding="utf-8")
    else:
        for result in results:
            if result["status"] == "passed":
                print(f"PASS {result['operation']} ({result['method']} {result['path']}) {result['durationMs']}ms")
            else:
                print(f"FAIL {result['operation']} ({result['method']} {result['path']})\n{result.get('error', '')}", file=sys.stderr)
        if not results:
            print("No code samples ran (empty SDK or a SCALAR_SMOKE_FILTER that matched nothing).", file=sys.stderr)
        else:
            print(f"\n{len(results) - len(failed)}/{len(results)} samples passed")

    if failed or not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
