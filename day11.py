#!/bin/python3

import math
import os
import random
import re
import sys

def sum_hourglass1(hourglass):
    sum = 0
    for i in range(len(hourglass)):
        for j in range(len(hourglass)):
            if i != 1:
                sum = sum + hourglass[i][j]
            elif i == 1 and j == 1:
                sum = sum + hourglass[i][j]
    return sum


if __name__ == '__main__':
    arr = []
    hourglasses = []
    hourglasses_tmp = []
    hourglasses_tmp_min = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    len_arr = len(arr[0])
    for mm in range(4):
        for ii in range(4):
            for jj in range(mm, mm+3):
                hourglasses_tmp_min=arr[jj][ii:ii+3]
                hourglasses_tmp.append(hourglasses_tmp_min)
                # print(hourglasses_tmp)
                hourglasses_tmp_min=[]
            hourglasses.append(hourglasses_tmp)
            hourglasses_tmp=[]
    # print(hourglasses)
    # second sum every hourglass from hourglasses
    # and append a list, and sort reverse=True, the first value=list[0] is you want.
    sum_hourglasses_list = []
    for hourglass in hourglasses:
        sum_hourglasses_list.append(sum_hourglass1(hourglass))
    sum_hourglasses_list.sort(reverse=True)
    print(sum_hourglasses_list[0])

    