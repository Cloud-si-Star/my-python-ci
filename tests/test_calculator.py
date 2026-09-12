import pytest
from my_package.calculator import add, divide

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

@pytest.mark.parametrize(
    'case',
    [
        {'id':10001},
        {'id':10002}
    ]
)
def test_use_code(case):

    assert case["id"]==10001
    assert True