from day_2_pgg.cw_4 import is_prime

def test_pgg_simple():
    assert is_prime(2) == True
    assert is_prime(5) == True
    assert is_prime(12) == False
    assert is_prime(-10) == False

    for x in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        assert is_prime(x) == True

    for x in [-10, -1, 0, 1]:
        assert is_prime(x) is False


def test_is_prime_basic_number():
    # Given When Then
    
    # given
    number = 5
    
    # when
    result = is_prime(number)

    # then 
    assert result == True
    assert result is True  # tak najlepiej porownywac z booleanem
    assert result  # w przypadku funkcji is_prime nawet nie musimy stricte porownywac z bool
