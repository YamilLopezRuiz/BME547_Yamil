import pytest


@pytest.mark.parametrize("x, y, test, expected", [
 ([1, 1], [2, 2], 3, 3),  # Only letters
 ([1, 2], [2, 1], 3, 0),  # Only numbers
 ([2, 13], [8, 37], 45, 185),  # Letters and numbers
 ([-3, 28], [5, -12], 6, -17)  # Letters and dash
 ])
def test_find_third_point(x, y, test, expected):
    from Feb03_assignment import find_third_point
    answer = find_third_point(x, y, test)
    assert answer == expected


@pytest.mark.parametrize("first, second, third, expected", [
 ([1, 1], [2, 2], [3, 3], True),  # Only letters
 ([1, 1], [2, 2], [3, 2], False),  # Only numbers
 ([-3, 28], [5, -12], [6, -17], True),  # Letters and numbers
 ([-3, 28], [5, -12], [2, -17], False)  # Letters and dash
 ])
def test_check_new_point(first, second, third, expected):
    from Feb03_assignment import check_new_point
    answer = check_new_point(first, second, third)
    assert answer == expected
