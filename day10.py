#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
	n = int(input())
	quot = 0 # quotient 商
	rem = 0  # remainder 余数
	count = 0 # Number of consecutive 1 连续1的个数
	Maximum = 0 # Maximum number of consecutive 's 连续1的个数的最大值
	while n != 0:
		quot = int(n / 2) # 这里要用int类型，否则默认的是float类型，出现错误
		rem = int(n % 2)  # 这里要用int类型，否则默认的是float类型，出现错误
		if rem == 1:
			count += 1
			if count > Maximum:
				Maximum = count
		else:
			count = 0
		n = quot
	print(Maximum)

        
        




