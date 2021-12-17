# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 17:09:58 2021

@author: Dell
"""
class Node:
    def __init__(self,data=None):
        self.previous=None
        self.data=data
        self.next=None
class tail:
    def __init__(self):
        self.tpointer=None
class head:
    def __init__(self):
        self.pointer=None

 
l1=head() 
l2=tail()             
n1=Node('Gregory')
n2=Node('Sam')
n3=Node('Linda')
n4=Node('John')
n5=Node('Aiden')

l1.pointer1=n1
n1.previous=None
n1.next=n2
n2.previous=n1
n2.next=n3
n3.previous=n2
n3.next=n4
n4.previous=n3
n4.next=n5
n5.previous=n4
n5.next=None
l2.tpointer=n5


def Iterate():
    printVal=l1.pointer
    while printVal is not None:
        print(printVal.data)
        printVal=printVal.next


#insert between two nodes
def Insert(name,node1,node2):
      
    if node1.next!=node2:
      print("Those two nodes are not connected")
      
    elif node1.next==node2:    
      newnode=Node(name)
      
      node1.next=newnode
      newnode.previous=node1
      newnode.next=node2
      node2.previous=newnode
      print('#####################after new node###########################')
      Iterate()
      Reverse()
       
def Reverse():
    
    print('#####################################################')
    print('Now For The Reverse')
    print('#####################################################')
     
    printVal=l2.tpointer
    while printVal is not None:
        print(printVal.data)
        printVal=printVal.previous

#insert at the beginning
def Beginning(name):
    newnode1=Node(name)
    newnode1.previous=None
    newnode1.next=n1
    n1.previous=newnode1
    l1.pointer=newnode1
    print('#####################after new node at beginning ###########################')
    Iterate()
    Reverse()
 
def Last(name):
    newnode2=Node(name)
    newnode2.previous=n5
    newnode2.next=None
    n5.next=newnode2
    
    print('#####################after new node at End ###########################')
    
    Iterate()
    l2.tpointer=newnode2
    Reverse()
    
    
Iterate()
Reverse()
Insert('Jenny',n2,n3)
Beginning('Kenny')
Last('Sally')