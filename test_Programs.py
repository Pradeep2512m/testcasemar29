import Programs

import pytest

@pytest.mark.parametrize("a,b",[(153,True),(370,True),(371,False),(407,True)])

def test_AmstrongorNot(a,b):
    result = Programs.AmstrongNumber(a)
    assert result == b

@pytest.mark.parametrize("a,b",[(8,True),(10,False),(88,True),(73,True)])
@pytest.mark.skip(reason = "no need")

def test_Divisibleby8(a,b):
    result = Programs.Div_8(a)
    assert result == b

@pytest.mark.parametrize("a,b,c,d",[(2,1,4,1),(4,2,5,2),(15,10,14,10),(12,32,34,10),(13,8,6,17)])
@pytest.mark.xfail

def test_Smallest(a,b,c,d):
    result = Programs.Smallest(a,b,c)
    assert result == d

@pytest.mark.parametrize("a, b",[(12,True),(15,False),(14,True)])

def test_Evenorodd(a,b):
    result = Programs.EvenorOdd(a)
    assert result == b

@pytest.mark.parametrize("a,b",[("121",True),("232",True),("1551",True),("120",True),("221",True)])
def test_Palindrome(a,b):
    result = Programs.PalindromeorNot(a)
    assert result == b