from Development.Session import addition 

# check add positive number
def test_addPositive():
  assert addition(4,2) == 6
  
# check if properly adds Zero 
def test_addZero():
  assert addition(4,0) == 4

# check with negative numbers
def test_addNegative():
  assert addition(4,-100) == -96