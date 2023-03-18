#!/bin/python3

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY an as parameter.
#

def reverseArray(a):
    """
    Return a reverse of a.
    :param a: list to reverse
    :return: list reversed
    """
    return reversed(a)


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(' '.join(map(str, res)))
