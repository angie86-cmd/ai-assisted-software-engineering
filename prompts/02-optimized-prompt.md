# Case Study 01 - Optimized Prompt

## Background

The weak prompt defined the general goal, but did not provide enough engineering detail to produce a consistent, testable and maintainable result.

This optimized prompt reformulates the task as a small software engineering specification.

## Scenario

An engineer wants to use an AI assistant to generate a Python implementation of the Fibonacci sequence that can be reviewed, tested and reused.

## Optimized Prompt

Create a Python 3 implementation of the Fibonacci sequence.

Requirements:

- Implement a function named `fibonacci(n)`.
- The function must return the first `n` Fibonacci numbers as a list of integers.
- Use type hints.
- Add a clear docstring explaining the function behavior, parameters, return value and possible exceptions.
- Validate the input:
  - raise `TypeError` if `n` is not an integer.
  - raise `ValueError` if `n` is negative.
- Use an iterative implementation to keep the solution simple and efficient.
- Follow PEP 8 style guidelines.
- Add unit tests using `pytest`.
- Include tests for:
  - `n = 0`
  - `n = 1`
  - a typical valid input such as `n = 10`
  - negative input
  - non-integer input

## Expected Output

The result should include:

- a Python source file containing the implementation
- a pytest test file validating the expected behavior
- code that is readable, maintainable and easy to review

## Engineering Perspective

This prompt improves the quality of the AI-generated result by transforming a vague programming request into a verifiable software specification.

It defines the expected interface, output format, validation rules, implementation style and testing criteria.