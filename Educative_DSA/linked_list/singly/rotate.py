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

    def rotate(self,pivot):
        p = self.head
        q = self.head
        prev = None
        count = 0

        while p and count<pivot:
            prev = p
            p = p.next 
            q = q.next 
            count += 1
        p = prev
        while q:
            prev = q 
            q = q.next 
        q = prev 

        q.next = self.head 
        self.head = p.next 
        p.next = None

    def tail_to_head(self):
        p = self.head
        q = self.head
        #n = self.get_length()
        count = 0
        prev = None
        while p and p.next:
            prev = p
            p = p.next
            q = q.next
            count += 1
        prev.next = None
        q.next = self.head
        self.head = q
        
    
    def print_list(self):               #print the list
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

LL = LinkedList()
LL.append(10)
LL.append(22)
LL.append(67)
LL.append(43)
LL.append(60)
LL.print_list()
LL.tail_to_head()
print("tail to head")
LL.print_list()