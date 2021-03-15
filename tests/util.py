import uuid
from pathlib import Path

import pytest
import responses

import hypervector


def get_resource_path(filename):
    resources_dir = str(Path(__file__).parent) + "/resources/"
    return resources_dir + filename


def mocked_resources(mocked_responses):
    # definition
    mocked_responses.add(
        responses.POST,
        f'{hypervector.API_BASE}/definition/add',
        json={
            "definition_uuid": str(uuid.uuid4()),
            "definition_name": "Mocked definition",
            "project_uuid": str(uuid.uuid4()),
            "added": "Mon, 1 Jan 1970 00:00:00 GMT"
        }
    )

    definition = hypervector.Definition.new(
        definition_file=get_resource_path("hyperdef.json"),
        project_uuid=str(uuid.uuid4())
    )

    mocked_responses.add(
        responses.GET,
        f'{hypervector.API_BASE}/definition/{definition.definition_uuid}',
        json=definition.to_response()
    )

    # ensemble
    ensemble_size = 100

    mocked_responses.add(
        responses.POST,
        f'{hypervector.API_BASE}/definition/{definition.definition_uuid}/ensembles/add',
        json={
            "ensemble_name": "echo-stop-ide-eigen",
            "ensemble_uuid": str(uuid.uuid4()),
            "definition_uuid": definition.definition_uuid,
            "added": "Mon, 1 Jan 1970 00:00:01 GMT",
            "size": ensemble_size
        }
    )

    ensemble = hypervector.Ensemble.new(
        definition_uuid=definition.definition_uuid,
        size=ensemble_size
    )

    mocked_responses.add(
        responses.GET,
        f'{hypervector.API_BASE}/ensemble/{ensemble.ensemble_uuid}',
        json=ensemble.to_response()
    )

    # benchmark
    mocked_responses.add(
        responses.POST,
        f'{hypervector.API_BASE}/definition/{ensemble.definition_uuid}'
        f'/ensemble/{ensemble.ensemble_uuid}/benchmarks/add',
        json={
            "benchmark_uuid": str(uuid.uuid4()),
            "added": "Mon, 1 Jan 1970 00:00:02 GMT",
            "ensemble_uuid": ensemble.ensemble_uuid,
            "definition_uuid": ensemble.definition_uuid
        }
    )

    benchmark = hypervector.Benchmark.new(
        ensemble=ensemble,
        expected_output=[1 for _ in range(ensemble.size)]
    )

    mocked_responses.add(
        responses.GET,
        f'{hypervector.API_BASE}/benchmark/{benchmark.benchmark_uuid}',
        json=benchmark.to_response()
    )

    return definition, ensemble, benchmark

