import hypervector


def test_ensemble():
    ensembles = hypervector.Ensemble.list()
    assert isinstance(ensembles[0], hypervector.Ensemble)