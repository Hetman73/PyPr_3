import pytest

from src.processing import filter_by_state
from tests.conftest import filter_by_state_input


@pytest.mark.parametrize(["source_list", "state", "expected_result"], filter_by_state_input())
def test_filter_by_state(source_list, state, expected_result):
    assert filter_by_state(source_list, state) == expected_result
