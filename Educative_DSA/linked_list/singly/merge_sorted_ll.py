class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    #insertion operation

    def append(self,data):               #insert at the end
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node

    def print_list(self):               #print the list
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next 

    def merge_sorted(self, llist):

        p = self.head 
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p 
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s 
        while p and q:
            if p.data <= q.data:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q 
        if not q:
            s.next = p

        self.head = new_head     
        return self.head

#linked list 1
LL = LinkedList()
LL.append(4)
LL.append(5)
LL.append(56)
LL.append(89)

#linked list 2
LL2 = LinkedList()
LL2.append(3)
LL2.append(43)
LL2.append(67)
LL.merge_sorted(LL2)
#merged linke list
LL.print_list()