#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    res = []  # Initialize the result list
    if n > 0:  # Check if n is greater than 0
        for i in range(1, n + 1):  # Loop through 1 to n (inclusive)
            level = []  # Initialize the current level list
            C = 1  # Start with the binomial coefficient C(i, 0)
            for j in range(1, i + 1):  # Loop to fill in the current row
                level.append(C)  # Append the current binomial coefficient to the level
                C = C * (i - j) // j  # Compute the next binomial coefficient
            res.append(level)  # Append the current level to the result
    return res  # Return the result list
