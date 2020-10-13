from list import *
class Node:
    def __init__(self,initval=None):
      self.value=initval
      self.next=None
      return
    def isempty(self):
        return(self.value==None)
    def length(self):
        if self.value == None:
            return(0)
        elif self.next == None:
            return(1)
        else:
            return(1+self.next.length())
    def append(self,v):
        if(self.isempty()):
            self.value=v
        elif self.next==None:
            newnode=Node(v)
            self.next=newnode
        else:
            (self.next).append(v)
        return()
    def insert(self ,v):
        if self.isempty():
            self.value=v
            return
        newnode=Node(v)
        (self.value,newnode.value)=(newnode.value,self.value)
        (self.next,newnode.next)=(newnode,self.next)
        return()
    def __str__(self):
        selflist=[]
        if self.value==None:
            return(str(selflist))
        temp=self
        selflist.append(temp.value)
        while temp.next !=None:
            temp=temp.next
            selflist.append(temp.value)
        return(str(selflist))
n1=Node(3)
n1.append(5)
n1.append(2)
n1.append(2)
n1.append(2)

n1.append(8)
n1.append(6)
print(n1.length())