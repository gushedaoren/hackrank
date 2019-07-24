#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    nmap={}

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if emailID.endswith("@gmail.com"):
            key=emailID.replace("@gmail.com","")
            nmap[key]=firstName
  
    items=nmap.values()
    items2=sorted(items)
    
    for key in items2:
        print(key)

    

