class SinglyNode:
  def __init__(self,val,next=None):
    self.val=val
    self.next=next


    def __str__(self):
      return str(self.val)
    

Head=SinglyNode(1)
A=SinglyNode(3)
B=SinglyNode(5)
C = SinglyNode(7)

Head.next=A
A.next=B
B.next=C


# print(A.val)
# Traverse LinkedList
curr = Head

# while curr:
#   print(curr.val)
#   curr = curr.next

#---------------------------------------------------
#Display Linked List - O(n)

# def display(Head):
#   curr=Head
#   elements=[]
#   while curr:
#     elements.append(str(curr.val))
#     curr=curr.next
#   print("->".join(elements))

# display(Head)

#--------------------------------

#search for node value -O(n)

def search(head,val):
  curr=head
  while curr:
    if val==curr.val:
      return True
    curr=curr.next
  return False

s=search(Head,2)
print(s)

