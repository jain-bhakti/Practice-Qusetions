class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+'-->'
            itr = itr.next
        print(llstr)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return 

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None) 

    def insert_at(self,data,index):
        if index > self.get_length():
            print("Index out of range to insert value")
            return 

        if index ==0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node

            itr = itr.next
            count += 1
    
    def insert_by_value(self,value, data):
        itr = self.head
        while itr:
            if itr.data == value:
                node = Node(data,itr.next)
                itr.next = node

            itr = itr.next


ll = Linked_List()
ll.insert_at_end(24)
ll.insert_at_end(75)
ll.insert_at(32,2)
ll.insert_by_value(75,2)
ll.print()
print(ll.get_length())
