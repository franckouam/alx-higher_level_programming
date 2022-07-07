#!/usr/bin/python3

"""
Pascal triangle module
"""


def pascal_triangle(n):
    """Returns a list of list of integers representing
    the Pascal's triangle of n"""
    P = []
    if n > 0:
        for i in range(n):
            L = [1 for _ in range(i+1)]
            for j in range(i):
                if j != 0 and j != i:
                    L[j] = P[i-1][j] + P[i-1][j-1]
            P.append(L)
    return P
