# Test things that have an input & output, doesn't require user intervention

import pytest
# Add a decorator, allows the function to run many times
# Give it a string of the parameters you want in a string, separated by a comma
# Then in a list, put all possible different inputs


@pytest.mark.parametrize("HDL_input, expected",
                         [(65, "Normal"), (45, "Borderline Low"), (20, "Low")])


def test_HDL_analysis(HDL_input, expected):
    from blood_calculator import HDL_analysis
    # Arrange
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == expected
    # Multiple test in same call: don't do bc if one fails it stops


@pytest.mark.parametrize("LDL_input, expected",
                         [(120, "Normal"), (140, "Borderline High"),
                          (180, "High"), (200, "Very High")])


def test_LDL_analysis(LDL_input, expected):
    from blood_calculator import LDL_analysis
    # Arrange
    answer = LDL_analysis(LDL_input)
    # Assert
    assert answer == expected


def test_chol_analysis():
    from blood_calculator import chol_analysis
    # Arrange
    chol_input = 220
    # Act
    answer = chol_analysis(chol_input)
    # Assert
    assert answer == "Borderline High"


def test_chol_analysis_High():
    from blood_calculator import chol_analysis
    # Arrange
    chol_input = 260
    # Act
    answer = chol_analysis(chol_input)
    # Assert
    assert answer == "High"
