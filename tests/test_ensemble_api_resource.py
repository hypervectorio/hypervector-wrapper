import hypervector
from tests.util import get_resource_path


def test_ensemble_list():
    definition = hypervector.Definition.list()[0]
    ensembles = hypervector.Ensemble.list(definition)

    for ensemble in ensembles:
        assert isinstance(ensemble, hypervector.Ensemble)


def test_ensemble_new():
    new_project = hypervector.Project.new()
    new_definition = hypervector.Definition.new(
        project_uuid=new_project.project_uuid,
        definition_file=get_resource_path("hyperdef.json")
    )
    ensemble = hypervector.Ensemble.new(
        new_definition.definition_uuid,
        'MEDIUM'
    )

    assert isinstance(ensemble, hypervector.Ensemble)


def test_ensemble_get():
    definition = hypervector.Definition.list()[0]
    ensemble_uuids = [ensemble.ensemble_uuid
                      for ensemble in hypervector.Ensemble.list(definition)]

    for ensemble_uuid in ensemble_uuids:
        ensemble = hypervector.Ensemble.get(ensemble_uuid)
        assert len(ensemble.hypervectors) == ensemble.size

        if ensemble.benchmarks is not None:
            for benchmark in ensemble.benchmarks:
                assert isinstance(benchmark, hypervector.Benchmark)