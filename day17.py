#Write your code here
import math
class Calculator:
    def power(self,n,p):
        if (n<0)|(p<0):
            raise Exception("n and p should be non-negative")
        else:
            ans = int(math.pow(n,p))
            return ans

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   