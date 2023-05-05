class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head is None:
            self.head = Node(data)
        
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def prepend(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node


    def add_after(self,key,data):
        cur = self.head
        while cur.next:
            if cur.data == key:
                new_node = Node(data)
                new_node.next = cur.next
                new_node.prev = cur
                cur.next = new_node
                break
            cur = cur.next

    def add_before(self,key,data):
        cur = self.head
        while cur.next:
            if cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
                break
            cur = cur.next

    def delete_head(self):
        self.head = self.head.next
        self.head.prev = None

    def delete_between(self,key):
        cur = self.head
        pre = None
        nex = None
        while cur.next:
            pre = cur.prev
            if cur.data == key:
                pre.next = cur.next
                nex = cur.next
                nex.prev = pre

            cur = cur.next

    def delete_tail(self):
        cur = self.head
        while cur:
            if not cur.next:
                prev = cur.prev
                prev.next = None
                cur.prev = None
                cur = None
                return
            cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev


    def print_list(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next


DL = DoublyLL()
DL.append(76)
DL.append(89)
DL.append(34)
DL.prepend(6)


DL.reverse()
DL.print_list()