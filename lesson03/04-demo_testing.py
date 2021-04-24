def adder(lhs, rhs):
    return lhs + rhs


def test_adder_simple_add():
    assert adder(9, 10) == 19


def test_adder_floats():
    assert adder(1.1, 2.3) == 3.4

##test programs 

# test runner is capable of running tets (for example above code) with the names "test_"

#it's called pytest (you need to: pip install pytest)

# to test the above code, run the below ( -vv is for verbose logging )
# pytest -vv C:\Python\python-train\lesson03\03-demo_testing.py 

