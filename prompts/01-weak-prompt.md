# Case Study 01 - Weak Prompt

## Background

One of the earliest programming exercises encountered in computer science and engineering courses is the Fibonacci sequence.

This case study revisits that classic problem to explore how different prompt formulations influence AI-generated software artifacts.

## Scenario

A developer wants to generate a Python solution using an AI assistant but provides only a minimal instruction.

## Prompt

Create a Python program that calculates the Fibonacci sequence.

## Analysis

This prompt specifies the task but leaves many important engineering decisions undefined.

The prompt does not specify:

- the expected output format
- the function interface
- input validation rules
- error handling requirements
- coding standards
- documentation requirements
- testing requirements

As a result, different AI systems may generate significantly different implementations, making the outcome difficult to validate and compare.

## Engineering Perspective

From a software engineering perspective, this prompt resembles a requirement that defines a goal but lacks sufficient detail for consistent implementation and verification.