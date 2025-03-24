class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        current = self.head
        while current is not None:
            print(f"{current.data}", end=" -> ")
            current = current.next
        print("None")

    def insert(self, data, location):
        newnode = Node(data)
        if self.head is None and location == 0:
            self.head = newnode
            self.tail = newnode
            return
        elif self.head and location == 0:
            newnode.next = self.head
            self.head = newnode
            return
        elif self.head and location == -1:
            self.tail.next = newnode
            newnode.next = None
            self.tail = newnode
            return

        index = 1
        current = self.head
        while current is not None:
            if location == index:
                newnode.next = current.next
                current.next = newnode
                if newnode.next is None:
                    self.tail = newnode

            current = current.next
            index += 1

    def search(self, data):
        if self.head is None:
            print("the list is empty")
        elif self.head:
            current = self.head
            index = 0
            found = False
            while current is not None:
                if data == current.data:
                    print(f"the value is found its index is {index}")
                    found = True
                current = current.next
                index += 1
            if found == False:
                print("the valuse is not in the list")

    def deletenode(self, location):
        if self.head == None:
            print("the node is empty already")
        elif self.head and location == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            index = 1
            current = self.head
            while current is not None and current.next is not None:
                if index == location:
                    if current.next.next is None:
                        current.next = None
                        self.tail = current
                    else:
                        current.next = current.next.next
                current = current.next
                index += 1
