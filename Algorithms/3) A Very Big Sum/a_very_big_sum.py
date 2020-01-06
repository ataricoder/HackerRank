#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.


def aVeryBigSum(ar):
    sum = 0
    for i in range(len(ar)):
        sum += ar[i]
    return sum


def main():

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)


main()
5
