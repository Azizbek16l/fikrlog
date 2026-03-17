from testlesson.add import add
import pytest

# simple example
# def test_add():
#     expected=2
#     got=add(1,1)
    
#     assert got == expected, f"{expected=}, {got=}"
    
# table method 
@pytest.mark.parametrize("a,b,expected",[
        (1,2,3),
        (2,2,4),
        (0,1,1),
        (-2,2,0)
    ])
def test_add(a,b,expected):  
        got=add(a,b)
        assert got == expected , f"{expected=}, {got=} "
 
     
          
