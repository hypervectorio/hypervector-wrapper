import pytest
import responses

import hypervector
from tests import util

hypervector.API_KEY = "dummy_value_not_a_valid_api_key"


@pytest.fixture
def mocked_responses():
    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        yield rsps


@pytest.fixture
def mocked_resources(mocked_responses):
    return util.mocked_resources(mocked_responses)