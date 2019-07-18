# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
mm = {}
for i in range(0,n):
    inputstr = input()
    arr = inputstr.split(" ",1)
    mm[arr[0]] = arr[1]

for i in range(0,n):
    inputstr = input()
    if inputstr in mm:
        print(inputstr+"="+mm[inputstr])
    else:
        print("Not found")