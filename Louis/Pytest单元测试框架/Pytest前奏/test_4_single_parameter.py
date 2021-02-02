__author__ = 'Louis-Pan'

import pytest

@pytest.mark.parametrize("x",[
    (1),
    (3),
    (5)
    ])

def test_equal(x):
    assert x in [i for i in range(1,6)]
