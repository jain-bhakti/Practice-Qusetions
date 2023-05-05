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

    def length(self):
        count = 1
        cur = self.head
        while cur:
            cur = cur.next
            count += 1
            if cur.next == self.head:
                break
        return count

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def split_into_half(self):
        size = self.length()
      
        mid = size//2
        if size == 0:
            return None
        if size == 1:
            return self.head

        count = 0
        cur = self.head
        prev = None

        while cur and count<mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        new_cl = Circular_llist()

        while cur.next != self.head:
            new_cl.append(cur.data)
            cur = cur.next
        new_cl.append(cur.data)

        self.print_list()
        print("\n")
        new_cl.print_list()

CL = Circular_llist()
CL.append(12)
CL.append(32)
CL.append(45)
CL.append(34)
CL.append(67)
CL.append(89)
CL.split_into_half()
