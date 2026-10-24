from src.processing import filter_by_state


def test_filter_by_state(filter_by_state_input):
    source_list, state, expected_result = filter_by_state_input
    assert filter_by_state(source_list, state) == expected_result
