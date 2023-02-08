import pytest

def test_add():
    from add import add
    answer = add(0.1, 0.2)
    assert answer == pytest.approx(0.3)
    #will fail if 0.1 + 0.2 = 0.3 bc converting values gives a slight residue
    #need to have test that says approximately is that value