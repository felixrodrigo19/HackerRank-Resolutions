#!/bin/python3

import math
import os
import random
import re
import sys


def calculate_hourglass(arr, initial_line, initial_column):
    row_begin = (
            arr[initial_line][initial_column] +
            arr[initial_line][initial_column + 1] +
            arr[initial_line][initial_column + 2]
    )
    row_center = arr[initial_line + 1][initial_column + 1]
    row_end = (
            arr[initial_line + 2][initial_column] +
            arr[initial_line + 2][initial_column + 1] +
            arr[initial_line + 2][initial_column + 2]
    )
    return row_begin + row_center + row_end


def hourglassSum(arr):
    values = [calculate_hourglass(arr, initial_line, initial_column)
              for initial_line in range(0, 4)
              for initial_column in range(0, 4)]
    return max(values)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
