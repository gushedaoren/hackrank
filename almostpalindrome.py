import string
def checkpalindrome(n): 
    count = 0
    z = len(n) - 1
    mp=dict.fromkeys(string.ascii_lowercase,0)
    if n ==n[::-1]:
        return "YES"
    memo = []
    for i in range(len(n)//2):
        if n[i] != n[z]:
            count += 1
            memo.append(i)
        mp[n[i]] += 1
        z -= 1    
    if count > 2:
        return "NO"
    if count == 2:
        return "YES"
    if count == 1 and len(n) % 2 == 0:
        return "No"
    if count == 1 and len(n) % 2 == 1:
        return "YES"
    if count == 0:
        return "YES"


		
		
if __name__ == '__main__':
	str = input()
	flag=False
	if (len(str)<=1)|(len(str)>500000):
		print("ERROR INPUT")
	else:
		
		if checkpalindrome(str)=="YES":
			flag=True
		
		else:
			flag=False
	

		if flag==True:	
			print("YES")		
		else:
			print("NO")