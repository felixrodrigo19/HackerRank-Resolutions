#!/bin/python3

import math
import os
import random
import re
import sys


def calculate_hourglass(arr, line_index, column_index):
    row_begin = (
            arr[line_index][column_index] +
            arr[line_index][column_index + 1] +
            arr[line_index][column_index + 2]
    )
    row_center = arr[line_index + 1][column_index + 1]
    row_end = (
            arr[line_index + 2][column_index] +
            arr[line_index + 2][column_index + 1] +
            arr[line_index + 2][column_index + 2]
    )
    return row_begin + row_center + row_end


def hourglassSum(arr):
    values = [calculate_hourglass(arr, line_index, column_index)
              for line_index in range(0, 4)
              for column_index in range(0, 4)]
    return max(values)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
