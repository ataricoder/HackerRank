#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.


def compareTriplets(a, b):
    alicePoints = 0
    bobPoints = 0
    for i in range(len(a)):
        if (a[i] > b[i]):
            alicePoints += 1
        if (a[i] < b[i]):
            bobPoints += 1
    return alicePoints, bobPoints


def main():

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)


main()
