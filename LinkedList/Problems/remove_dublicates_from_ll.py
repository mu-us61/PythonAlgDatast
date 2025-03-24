# remove dublicates from an unsorted linked list
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __str__(self):
        if self.head == None:
            return "Empty List"
        else:
            current=self.head
            values=[]
            while current:
                values.append(str(current.value))
                current = current.next
                if current == None:
                    break
            return " -> ".join(values)
            
    def add(self,value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
            
#     def remove_dublicates(self):
#         if self.head==None:
#             print("the list is empty")
#         else:
#             single=[]
#             prev=self.head
#             current=prev.next
#             single.append(self.head.value)
#             
#             while current:
#                 if current.value not in single:
#                     single.append(current.value)
#                 else:
#                     prev.next=current.next # if current dub then remove
#                     if current is self.tail: # check edge case if removed one is tail, reassign tail
#                         self.tail = prev
#                         
#                 prev=prev.next
#                 current = current.next
#                 if current.next is None:
#                     break
        
    def remove_dublicates(self):
        if self.head == None:
            print("the list is empty")
        else:
            temp=self.head
            single=[]
            single.append(temp.value)
            while temp != self.tail: 
                if temp.next.value not in single:
                    single.append(temp.next.value)
                else:
                    temp.next=temp.next.next
                    if temp.next == None:
                        self.tail=temp.next
                temp =temp.next
        
        
        
            
ll = LinkedList()
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(4)
ll.add(6)
ll.add(4)
ll.add(8)
print(ll)
ll.remove_dublicates()
print(ll)
