def fibonacci(n):
    """Return a list of the first n Fibonacci numbers.

    This implementation follows the minimal requirement from the weak prompt:
    it calculates the Fibonacci sequence. No input validation is performed.
    """
    if n == 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq
