class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None
  
class DoublyLL:
  def __init__(self):
    self.head=None
  
  def print_LL(self):
    if self.head is None:
      print("LinkedList is empty")
    else:
      n=self.head
      while n:
        print(n.data,"-->",end=" ")
        n=n.next
  def print_LL_reverse(self):
    print()
    if self.head is None:
      print("LinkedList is Empty")
    else:
      n=self.head
      while n.next is not None:
        n=n.next
      while n:
        print(n.data,"-->",end=" ")
        n=n.prev
    
  def insert_empty(self,data):
    if self.head is None:
      new_node=Node(data)
      self.head=new_node
    else:
      print("LinkedList is not Empty")
  def insert_at_begin(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=data
    else:
      new_node.next=self.head
      self.head.prev=new_node
      self.head=new_node
  def insert_at_end(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
    else:
      n=self.head
      while n.next is not None:
        n=n.next
      n.next=new_node
      new_node.prev=n
  def add_after(self,data,x):
    if self.head is None:
      print("LL is Empty")
    else:
      n=self.head
    while n is not None:
      if x == n.data:
        break
      n=n.next
    if n is None:
      print("Given Node is not present in DLL")
    else:
      new_node=Node(data)
      new_node.next=n.next
      new_node.prev=n
      if n.next is not None:
        n.next.prev=new_node
      n.next=new_node
  def add_before(self,data,x):
    if self.head is None:
      print("LL is Empty")
    else:
      n=self.head
    while n is not None:
      if x == n.data:
        break
      n=n.next
    if n is None:
      print("Given Node is not present in DLL")
    else:
      new_node=Node(data)
      new_node.next=n
      new_node.prev=n.prev
      if n.prev is not None:
        n.prev.next=new_node
      else:
        self.head=new_node
      n.prev=new_node
  def delete_begin(self):
    if self.head is None:
      print("DLL is empty can't delete")
      return
    if self.head.next==None:
      self.head=None
      print("DLL is Empty after deleting the node!")
    else:
      self.head=self.head.next
      self.head.prev=None
  def delete_after(self):
    if self.head is None:
      print("DLL is empty can't delete")
      return
    if self.head.next==None:
      self.head=None
      print("DLL is Empty after deleting the node!")
    else:
      n=self.head
      while n.next is not None:
        n=n.next
      n.prev.next=None
  def delete_by_value(self,x):
    if self.head is None:
      print("DLL is empty can't delete")
      return
    if self.head.next is None:
      if x==self.head.data:
        self.head=None
        print("DLL is Empty after deleting the node!")
      else:
        print("x is not present in the DLL")
      return
    if self.head.data == x:
      self.head=self.head.next
      self.head.prev=None
      return
    n=self.head
    while n.next is not None:
      if x == n.data:
        break
      n=n.next
    if n.next is not None:
      n.prev.next=n.next
      n.next.prev=n.prev
    else:
      if n.data==x:
        n.prev.next=None
      else:
        print("x is not presnt in DLL")








dl1=DoublyLL()
dl1.insert_empty(20)
dl1.insert_at_begin(10)
dl1.insert_at_end(30)
dl1.add_before(5,10)
dl1.delete_by_value(50)


dl1.print_LL()
