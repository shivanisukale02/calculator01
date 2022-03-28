import Calculator01

def test_add():
    x=10
    y=25
    result=Calculator01.add(x,y)
    assert x+y==result

def test_sub():
    x=30
    y=25
    result=Calculator01.sub(x,y)
    assert x-y==result

def test_mul():
    x=10
    y=25
    result=Calculator01.mul(x,y)
    assert x*y==result

def test_div():
    x=100
    y=25
    result=Calculator01.div(x,y)
    assert x/y==result
