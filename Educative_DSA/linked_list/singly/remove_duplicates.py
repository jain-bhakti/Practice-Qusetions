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

    def delete_by_value(self,value):
        cur_node = self.head
        if cur_node and cur_node.data == value:
            self.head = cur_node.next 
            cur_node = None
            return

        while cur_node:
            if cur_node.data != value:
                prev = cur_node
            else:
                prev.next = cur_node.next
            cur_node = cur_node.next
        
    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
            # Remove node:
                prev.next = cur.next
                cur = None
            else:
            # Have not encountered element before.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_list(self):               #print the list
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next


LL = LinkedList()
LL.append(1)
LL.append(4)
LL.append(4)
LL.append(4)
LL.append(12)
LL.remove_duplicates()
LL.print_list()