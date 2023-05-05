class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Circular_llist:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head

        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self,data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head
        if not self.head:
            self.head = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def remove(self,key):
        if self.head == key:
            cur = self.head
            if self.head.next == self.head:
                self.head = None
            else:
                while cur.next != self.head:
                    cur = cur.next
                cur.next = self.head.next
        
        else:
            prev = None
            cur = self.head
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next


    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    
CL = Circular_llist()
CL.append(12)
CL.append(32)
CL.append(45)
CL.append(34)
CL.remove(45)
CL.print_list()    
