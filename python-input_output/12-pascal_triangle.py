#!/usr/bin/python3
""" Module that contains a function that return a list of lists of integers"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of Pascal's triangle

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # Every row starts with 1

        # Calculate the intermediate values of the new row
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)  # Add the new row to the triangle

    return triangle
