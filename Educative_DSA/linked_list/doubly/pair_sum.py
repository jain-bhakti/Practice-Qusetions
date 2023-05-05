class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


    def sum_pair(self,sum):
        cur = self.head
        result = []
        pair = None
        while cur:
            pair = cur.next
            while pair:
                if pair.data == (sum - cur.data):
                    result.append("(" + str(cur.data) + "," + str(pair.data) + ")")
                pair = pair.next

            cur = cur.next
        return result


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)
dllist.print_list()
print(dllist.sum_pair(5))



