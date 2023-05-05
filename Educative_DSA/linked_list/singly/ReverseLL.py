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

    #reversing the Linked List itertively
    def rev_itr(self):
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        self.head = prev

    #reversing the Linked List Recursively
    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)


    def print_list(self):               #print the list
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next


LL = LinkedList()
LL.append(4)
LL.append(25)
LL.append(56)
LL.append(15)
print("Original List")
LL.print_list()
LL.rev_itr()
print("Reversed List")
LL.print_list()