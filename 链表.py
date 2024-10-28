'''
linked list 是常用的数据结构，由一系列节点构成，每个节点包含数据域和指针域，指针域储存了下一个节点的地址，从而建立起各节点之间的线性关系
节点=数据域+指针域
'''
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Linknode:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    def atbeginning(self,newdate):
        Newnode=Node(newdate)
        Newnode.nextval=self.headval
        self.headval=Newnode
    def atend(self,newdate):
        Newnode=Node(newdate)
        if self.headval is None:# 空链表
            self.headval=Newnode
            return
        late=self.headval
        while(late.nextval):# 遍历至最后的节点
            late=late.nextval
        late.nextval=Newnode
    def length(self):
        cur=self.headval
        len=0
        while cur is not None:
            cur=cur.nextval
            len+=1
        return len
    def insert(self,index,newdate):
        if index<=0:
            self.atbegining(newdate)
        if index>(self.length()-1):
            self.atend(newdate)
        else:
            newnode=Node(newdate)
            cur=self.headval
            for i in range(index-1):
                cur=cur.nextval
            newnode.nextval=cur.nextval
            cur.nextval=newnode


list=Linknode()
list.headval=Node("mon")
e2=Node('tue')
e3=Node('wed')
list.headval.nextval=e2
e2.nextval=e3
list.listprint()
list.atbeginning('sun')
print('-------------')
list.listprint()
print('-------------')
list.atend('fuck')
list.listprint()
print('-------------')
list.insert(3,'23')
list.listprint()

