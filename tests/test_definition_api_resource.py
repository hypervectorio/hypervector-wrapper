import hypervector


def test_definition():
    definitions = hypervector.Definition.list()
    assert isinstance(definitions[0], hypervector.Definition)