# return the node backwards , like lists list[-1] = returns the last
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        
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
        
        
    def frombackward(self,place):
        if self.head == None:
            return print("The list is empty")
        else:
            mylen = self.__len__()
            if mylen +1 <= abs(place):
                return print("the asked place is way more then the index of the list")
            mylist = [i for i in range(mylen)]
            chosen = mylist[place]
            
            index=0
            current=self.head
            while current:
                if index == chosen:
                    break
                index = index +1
                current = current.next
            
            return print(f"the {place} value from the list is {current.data}")
            
            
            
            
            
ll=SLinkedList()
ll.add(5)
ll.add(4)
ll.add(3)
ll.add(2)
ll.add(1)
print(ll)
# ll.reverse()
# print(ll)
print(len(ll))
ll.frombackward(-5)
        
