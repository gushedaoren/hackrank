class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        item = None
        if isinstance(data, Node):
            item = data
        else:
            item = Node(data)
            # print(item)

        if head == None:
            head = item
            return head
        else:
            tmp = head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = item
            return head



mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  