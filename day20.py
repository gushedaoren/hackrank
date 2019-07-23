#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps=0
for i in range(n):
    for j in range(len(a)):
       
        if j<len(a)-1:

            if a[j]>a[j+1]:
            
                
                tmp=a[j]
                a[j]=a[j+1]
                a[j+1]=tmp
                
                numSwaps=numSwaps+1
 
        print(a)
    if numSwaps==0:
        break
    

print("Array is sorted in %d swaps."%numSwaps)
print("First Element: %d"%a[0])
print("Last Element: %d"%a[n-1])


