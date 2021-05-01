import gzip
import json
import uuid
from pathlib import Path
from random import randint

import responses

import hypervector


def get_resource_path(filename):
    resources_dir = str(Path(__file__).parent) + "/resources/"
    return resources_dir + filename


def mocked_resources(mocked_responses):
    # project
    mocked_responses.add(
        responses.POST,
        f'{hypervector.API_BASE}/project/new',
        json={
            "project_uuid": str(uuid.uuid4()),
            "project_name": "Mocked project",
            "added": "Mon, 1 Jan 1970 00:00:00 GMT",
            "definitions": []  # empty
        }
    )

    project = hypervector.Project.new()

    # definition
    mocked_responses.add(
        responses.POST,
        f'{hypervector.API_BASE}/definition/add',
        json={
            "definition_uuid": str(uuid.uuid4()),
            "definition_name": "Mocked definition",
            "project_uuid": project.project_uuid,
            "added": "Mon, 1 Jan 1970 00:00:00 GMT",
            "ensembles": []
        }
    )

    definition = hypervector.Definition.new(
        definition=get_resource_path("hyperdef.json"),
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
            "size": ensemble_size,
            "benchmarks": []
        }
    )

    ensemble = hypervector.Ensemble.new(
        definition_uuid=definition.definition_uuid,
        size=ensemble_size
    )

    mocked_responses.add(
        responses.GET,
        f'{hypervector.API_BASE}/ensemble/{ensemble.ensemble_uuid}',
        json={
            "ensemble_name": "echo-stop-ide-eigen",
            "ensemble_uuid": str(uuid.uuid4()),
            "definition_uuid": definition.definition_uuid,
            "added": "Mon, 1 Jan 1970 00:00:01 GMT",
            "size": ensemble_size,
            "benchmarks": []
        }
    )

    ensemble_data = {'hypervectors': [randint(1, 10) for _ in range(ensemble_size)]}
    compressed_ensemble_get = json.dumps(ensemble_data).encode('utf-8')

    mocked_responses.add(
        responses.GET,
        f'{hypervector.API_BASE}/ensemble/{ensemble.ensemble_uuid}/data',
        compressed_ensemble_get
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

    return project, definition, ensemble, benchmark

