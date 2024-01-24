"""Tests API for solving problem Length of Last Word"""

import pytest

from leetcode_0058_length_of_last_word import api


@pytest.mark.parametrize(
    ["result", "s"],
    (
        [5, "Hello World"],
        [4, "  test2 xxxxxx xxxxxxx xxxxxxxxx  "],
        [6, "1 12 123 1234 12345"],
    ),
)
def test_length_of_last_word(result, s) -> None:
    """Tests solution for problem Length of Last Word"""

    assert api.length_of_last_word(s) == result
