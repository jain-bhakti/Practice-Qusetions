class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_ll:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+'-->'
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.tail
        
        llstr = ''
        while itr:
            llstr += str(itr.data)+'-->'
            itr = itr.prev
        print(llstr)


    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

ll = Doubly_ll()
ll.insert_at_beginning(34)
ll.insert_at_beginning(45)
ll.insert_at_beginning(76)
ll.print_forward()
