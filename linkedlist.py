class Node:# 节点
    def __init__(self,date=None):
        self.date=date
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def listprint(self):
        cur=self.head
        while cur is not None:
            print(cur.date)
            cur=cur.next
    def len(self):
        cur=self.head
        count=0
        while cur is not None:
            count+=1
            cur=cur.next
        return count
    def add(self,newdate):
        cur=Node(newdate)
        cur.next=self.head
        self.head=cur
    def append(self,newdate):
        cur=self.head
        newnode=Node(newdate)
        while cur.next is not None:
            cur=cur.next
        cur.next=newnode
    def insert(self,index,newdate):
        newnode=Node(newdate)
        if index<=0:
            self.add(newdate)
        if index>=(len(self)-1):
            self.append(newdate)
        else:
            cur=self.head
            for i in range(index-1):
                cur=cur.next
            newnode.next=cur.next
            cur.next=newnode
    def pop(self,index):
        if index<=0:
            cur=self.head
            self.head=cur.next
        else:
            cur=self.head
            cur_late=self.head
            for i in range(index-2):
                cur_late=cur_late.next
            for i in range(index-1):
                cur=cur.next
            cur_late.next=cur.next
list=Linkedlist()
list.head=Node('mon')
while True:
    scanf=input()
    if scanf=='stop':
        break
    list.append(scanf)
list.listprint()
            

        
        

        
            