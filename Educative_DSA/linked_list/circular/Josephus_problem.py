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

    def remove(self,node):
        if self.head:
            if self.head == node:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next 
                    self.head = self.head.next
            else:
                cur = self.head 
                prev = None
                while cur.next != self.head:
                    prev = cur 
                    cur = cur.next 
                    if cur == node:
                        prev.next = cur.next
                        cur = cur.next

                        
    def Josephus(self,step):
        cur = self.head
        length = self.length()
        while length > 1:
            count = 1 
            while count != step:
                cur = cur.next 
                count += 1
            print("KILL:" + str(cur.data))
            self.remove(cur)
            cur = cur.next
            length -= 1

cllist = Circular_llist()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)
cllist.Josephus(2)
print("Winner :")
cllist.print_list()


        