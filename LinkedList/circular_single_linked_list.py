# circular single linked list

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
    
class CircularSingleLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        
    def print(self):
        current=self.head
        if current is None:
            print("the list is empty")
        else:
            while current != self.tail:
                print(f"{current.data}", end=" -> ")
                current=current.next
            print(f"{current.data} -> HEAD") # self.tail
        
    def insert(self,data,location):
        if self.head is None:
            newnode=Node(data)
            newnode.next=newnode
            self.head=newnode
            self.tail=newnode
        elif location == -1:
            newnode=Node(data)
            self.tail.next=newnode
            newnode.next=self.head
            self.tail=newnode
        elif location == 0:
            newnode=Node(data)
            self.tail.next=newnode
            newnode.next=self.head
            self.head=newnode
        else:
            index=0
            prev=self.head
            newnode=Node(data)
            while index != location-1:
                index = index+1
                prev=prev.next
            newnode.next=prev.next
            prev.next=newnode
            if prev ==self.tail:
                self.tail=newnode
    def search(self,value):
        found=False
        if self.head is None:
            print("the list is empty")
        else:
            index=0
            current=self.head
            while current != self.tail:
                if value == current.data:
                    print(f"the value is found at index {index}")
                    found=True
                index=index+1
                current=current.next
            if value == current.data:
                    print(f"the value is found at index {index} (tail)")
                    found=True
            if not found:
                print("the value is not on the list")
    def deletenode(self,location):
        if self.head == None:
            print("the node does not exist")
        elif location == 0:
            if self.tail.next == self.head:
                self.tail = None
                self.head = None
            else:
                self.tail.next = self.head.next
                self.head =self.head.next
        else:
            prev=self.head
            index=0
            while True:
                if index == location -1:
                    break
                index= index + 1
                prev = prev.next
                # Safeguard to prevent infinite loops
                if prev == self.head:
                    print("The location is out of range.")
                    return
            
            
            if prev.next == self.tail:
                self.tail=prev
                prev.next=self.head
                
            else:
                prev.next=prev.next.next
                
        
        
        
        
        

csll=CircularSingleLinkedList()
csll.insert(5,0)
csll.insert(4,1)
csll.insert(5,0)
csll.insert(6,2)
csll.insert(9,4)

csll.print()
# csll.search(5)
csll.deletenode(5)
csll.print()
