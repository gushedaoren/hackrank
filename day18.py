import sys

class Solution:
    # Write your code here
    # Write your code here
    def __init__(self):
        # self.size = size
        self.stack = []
        self.top = -1
        self.front = -1
        self.rear = -1
        self.queue = []
    def pushCharacter(self, strr):
        if self.isfull_stack():
            raise Exception("stack is full")
        else:
            self.stack.append(strr)
            self.top = self.top + 1

    def popCharacter(self):
        if self.isempty_stack():
            raise Exception("stack is empty")
        else:
            self.top = self.top - 1
            last = self.stack.pop()
            return last

    def isfull_stack(self):
        # return self.top + 1 == self.size
        return 0

    def isempty_stack(self):
        return self.top == -1

    def show_stack(self):
        return self.stack

    def enqueueCharacter(self, strr):
        if self.isfull_queue():
            raise Exception("queue is full")
        else:
            self.queue.append(strr)
            self.rear = self.rear + 1

    def dequeueCharacter(self):
        if self.isempty_queue():
            raise Exception("queue is empty")
        else:
            first = self.queue.pop(0)
            self.front = self.front + 1
            return first

    def isfull_queue(self):
        # return self.rear - self.front + 1 == self.size
        return 0

    def isempty_queue(self):
        return self.rear == self.front

    def show_queue(self):
        return self.queue



# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    