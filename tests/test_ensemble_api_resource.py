import hypervector
from tests.util import get_resource_path


def test_ensemble():
    ensembles = hypervector.Ensemble.list()
    assert isinstance(ensembles[0], hypervector.Ensemble)


def test_ensemble_new():
    new_project = hypervector.Project.new()
    new_definition = hypervector.Definition.new(project_uuid=new_project.project_uuid,
                                                definition_file=get_resource_path("hyperdef.json"))
    ensemble = hypervector.Ensemble.new(
        new_definition.definition_uuid,
        10000
    )

    assert isinstance(ensemble, hypervector.Ensemble)


def test_ensemble_get():
    ensembles = hypervector.Ensemble.list()

    assert 1 == 1