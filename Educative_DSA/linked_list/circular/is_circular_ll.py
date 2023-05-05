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

    def check_cl(self,l_list):
        itr = l_list.head
        
        while itr:
            itr = itr.next
            if not itr:
                return False 
            if itr.next == l_list.head:
                #flag = True
                return True
        
        return False


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



LL = LinkedList()
LL.append(34)
LL.append(69)
LL.append(41)

CL = Circular_llist()
CL.append(44)
CL.append(76)
CL.append(32)

print(CL.check_cl(LL))
