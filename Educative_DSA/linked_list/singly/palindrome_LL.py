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

    def palindrome(self):
        s = ""
        itr = self.head
        while itr:
            s += str(itr.data)
            itr = itr.next
        
        return s == s[::-1]

LL = LinkedList()
LL.append(1)
LL.append(2)
LL.append(2)
LL.append(3)

print(LL.palindrome())

    