from typing import List


def fibonacci(n: int) -> List[int]:
    """Return the first ``n`` Fibonacci numbers as a list of integers.

    This function uses an iterative approach to build the sequence.

    Parameters
    ----------
    n : int
        The number of Fibonacci numbers to return. Must be a non-negative
        integer.

    Returns
    -------
    List[int]
        A list of the first ``n`` Fibonacci numbers. For example,
        ``fibonacci(3)`` returns ``[0, 1, 1]``.

    Raises
    ------
    TypeError
        If ``n`` is not an integer.
    ValueError
        If ``n`` is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return []
    if n == 1:
        return [0]

    seq: List[int] = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq
