# partition , divide the list to 2 one side is greater or equal to given node
# other side is less than



class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
        
    def __str__(self):
        if self.head == None:
            return "The list is empty"
        else:
            current = self.head
            values=[]
            while current:
                values.append(str(current.data))                
                current = current.next
            return " -> ".join(values)
    
    def add(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next=newnode
            self.tail = newnode
            
            
    def __len__(self):
        len=0
        current = self.head
        while current:
            len = len+1
            current = current.next
        return len
    

            
        
        
def partition(ll,x):
    new=SLinkedList()
    for i in ll:
        if i.data >= x:
            new.add(i.data)
    for i in ll:
        if i.data < x:
            new.add(i.data)
    return new
        
    
            
            
            
            
ll=SLinkedList()
ll.add(5)
ll.add(7)
ll.add(1)
ll.add(9)
ll.add(2)
ll.add(6)
ll.add(3)
ll.add(99)
print(ll)
print(partition(ll,4))
print(ll)



        
