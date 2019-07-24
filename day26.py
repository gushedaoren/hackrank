# Enter your code here. Read input from STDIN. Print output to STDOUT
date1=[]
date2=[]
result3=0
def compare(date1,date2):
    if(int(date1[2])>int(date2[2])):
        return 1
    elif (int(date1[2])<int(date2[2])):
        return 0

    if(int(date1[1])>int(date2[1])):
        return 1
    elif (int(date1[1])<int(date2[1])):
        return 0

    if(int(date1[0])>int(date2[0])):
        return 1
    elif (int(date1[0])<int(date2[0])):
        return 0
    else:
        return 0
        
        
for i in range(2):
    date=str(input())
    if i==0:

        date1=date.split(" ")
    if i==1:
        date2=date.split(" ")
    
flag=compare(date1,date2)
if int(date1[2])-int(date2[2])>0:
    result3=10000

result2=(int(date1[1])-int(date2[1]))*500*flag
result1=(int(date1[0])-int(date2[0]))*15*flag



if result3>0:
    print(result3)
    
elif result2>0:
    print(result2)
elif result1>0:
    print(result1)
else:
    print(0)
     



