def factorial(n: int) -> int:
    """
    Calculate the factorial of a given number.

    :param int n: The factorial to calculate
    :return: The resultant factorial
    """
    if n < 0:
        raise ValueError(
            f"Invalid n: n must be a non-negative integer. "
            f"Got {n=}"
        )

    factorial: int = 1
    for idx in range(1, n + 1):
        factorial = factorial * idx
        
    return factorial
