from ..main import incr_addition

# Those are not really tests, hardcodig results
# to trigger passing or not passing


def test_success():
    # PASS
    assert incr_addition(1, 2) == 4


def test_fail():
    # SIMULATE FIXED TEST 
    assert  incr_addition(2, 2) == 5
