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

    def prepend(self,data):            #insert at the beginning
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self,value,data):     #insert after a particular value
        new_node = Node(data)
        itr = self.head
        while itr:
            if itr.data == value:
                new_node.next = itr.next
                itr.next = new_node
                new_node
            itr = itr.next

    #deletion Operation

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


    def delete_by_position(self,index):
        cur_node = self.head
        count = 0
        if cur_node and index == 0:
            self.head = cur_node.next 
            cur_node = None
            return
        while cur_node:
            if count != index:
                prev = cur_node
            else:
                prev.next = cur_node.next
            cur_node = cur_node.next
            count += 1
                
    #getting length of the linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next  
        return(count)       

    #Linked List traversal
    def print_list(self):               #print the list
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next


LL = LinkedList()
LL.append(4)
LL.append(5)
LL.append(56)
LL.prepend(89)
LL.insert_after(5,55)
LL.delete_by_value(89)
LL.delete_by_position(0)  #passing index of the node want to delete as argument
LL.get_length()
LL.print_list()