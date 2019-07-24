import math
T=int(input())
datas=[]
result=""
# 用到math库中的开平方函数sqrt
def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):   #也可以用num**0.5
        if num % i == 0:
            return False
        
    return True

for i in range(T):
    data=int(input())
    datas.append(data)
    if isprime(data):
        result=result+"Prime \n"
    else:
        result=result+"Not prime \n"

print(result,end="")


      