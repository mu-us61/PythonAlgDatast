# 1 > 4 > 6   is 641 a number , there are two list turn them into number after that sum them then aagain turn theresult into a list


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
    

            
        
    
        
    
            
            
            
            
# ll=SLinkedList()
# ll.add(5)
# ll.add(7)
# ll.add(1)
# ll.add(9)
# print(ll)
ll1=SLinkedList()
ll1.add(5)
ll1.add(7)
ll1.add(1)
print(ll1)
ll2=SLinkedList()
ll2.add(1)
ll2.add(1)
ll2.add(1)
print(ll2)



def sums(ll1,ll2):
    list_ll1=[]
    list_ll2=[]
    for i in ll1:
        list_ll1.append(i.data)
    for i in ll2:
        list_ll2.append(i.data)
    num1 = int("".join(map(str,list_ll1[::-1])))
    num2 = int("".join(map(str,list_ll2[::-1])))
    num3=num1+num2
    num3=str(num3)
    newll=SLinkedList()
    for i in num3[::-1]:
        newll.add(int(i))
    return newll

print(sums(ll1,ll2))
