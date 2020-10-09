import hypervector


def test_definition_list():
    definitions = hypervector.Definition.list()

    for definition in definitions:
        assert isinstance(definition, hypervector.Definition)