__author__ = 'Louis-Pan'

import pytest

@pytest.mark.parametrize("x,y",[(3+5,8),(3+2,7),(3*8,20),])
def test_add(x,y):   # 此处已经写死，必须是x，y与parametrize
    assert x == y

if __name__=="__main__":
    pytest.main(['-s','test_8_fixture_high_parameterize.py'])