import Calculator01
import pytest

@pytest.mark.xfail
@pytest.mark.parametrize("a,b,c",[(3,2,5),(10,12,15),(2,5,8),(7,8,15)])
def test_add(a,b,c):

    result=Calculator01.add(a,b)
    assert not c==result

@pytest.mark.parametrize("a,b,c",[(7,2,5),(27,12,15),(13,5,8),(7,8,15)])
def test_sub(a,b,c):
    result=Calculator01.sub(a,b)
    assert c==result

@pytest.mark.parametrize("a,b,c",[(1,2,2),(3,4,12),(11,12,23),(2,7,9)])
def test_mul(a,b,c):
    result=Calculator01.mul(a,b)
    assert c==result

@pytest.mark.parametrize("a,b,c",[(10,5,2),(5,2,2.5),(70,2,35),(10,3,5)])
def test_div(a,b,c):
    result=Calculator01.div(a,b)
    assert c==result
