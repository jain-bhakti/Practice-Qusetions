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
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next  
        return(count) 

    def sum_two_lists(self, llist):
        p = self.head  
        q = llist.head

        sum_llist = LinkedList()

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0 
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        return sum_llist

    def print_list(self):               #print the list
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next
    

LL1 = LinkedList()
LL1.append(5)
LL1.append(6)
LL1.append(3)
LL2 = LinkedList()
LL2.append(8)
LL2.append(4)
LL2.append(2)
result = LL1.sum_two_lists(LL2)
result.print_list()

        