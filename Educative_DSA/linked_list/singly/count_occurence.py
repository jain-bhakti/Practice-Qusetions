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


    def count_occurences(self,n):
        count = 0
        itr = self.head
        while itr:
            if itr.data == n:
                count += 1
            itr = itr.next
    
        print("{} : {}".format(n,count))


LL = LinkedList()
LL.append(4)
LL.append(5)
LL.append(56)
LL.append(5)
LL.count_occurences(5)