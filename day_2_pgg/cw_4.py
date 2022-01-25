"""
Napisz funkcję sprawdzającą, czy dana liczba jest liczbą pierwszą.

- sprawdzanie typu
- type hinting
- docstring
- funkcja zwraca True/False

Przykład użycia:
> is_prime(10)
False
> is_prime(17)
True
"""

def is_prime(number: int) -> bool:
    """
    Returns True if number if prime, False otherwise.
    :param number: Number to be tested if is prime.
    :return:
    """

    if type(number) is not int:
        # co tutaj zrobic???
        # return False
        # return None
        # return 'Zle dane!!! Przeczytaj dokumentacje!!!'
        # https://docs.python.org/3/library/exceptions.html#exception-hierarchy
        raise TypeError('Number is not int.')

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True


