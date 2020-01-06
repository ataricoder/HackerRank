#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    positive = 0
    negative = 0
    zeroes = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zeroes += 1
        elif arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
    positiveRatio = positive / len(arr)
    negativeRatio = negative / len(arr)
    zeroesRatio = zeroes / len(arr)
    print(positiveRatio)
    print(negativeRatio)
    print(zeroesRatio)


def main():
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


main()
