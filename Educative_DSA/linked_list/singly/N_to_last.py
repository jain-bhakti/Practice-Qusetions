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

    def N_to_last(self,n):
        if n > self.get_length():
            print("n is greater than the length of list")
            return
        if n>=0:
            count = 0
            itr = self.head
            while itr:
                if count >= n:
                    print(itr.data)
                count += 1
                itr = itr.next
        else:
            print("N should be a positive number")
            return 
        
LL = LinkedList()
LL.append(23)
LL.append(32)
LL.append(54)
LL.append(87)
LL.N_to_last(1)
            