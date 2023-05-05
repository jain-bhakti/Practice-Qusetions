class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

    def check_cycle(self,head):
        itr = head
        visited = set()
        while itr:
            if itr.val not in visited:
                visited.add(itr.val)
            else:
                return itr
            itr = itr.next

        return -1

    def detect_cycle(self,head):

        """Taurus and the hair algorithm:
        1. take 2 pointers say, slow and fast
            --> slow moves one step at a time 
            --> fast moves two steps at a time
        2. Iterate till fast becomes equal to slow, i.e. both pointers coincide
        3. now initialize a new pointer say slow2 to head
        4.Iterate through and check
            --> if slow == slow2 : return slow
            --> increment slow and slow2 to their next pointer
        5. check whether the fast or next to is None:
            --> if yes, then return None. (NO CYCLE)"""

        if not head:
            return
            

        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break
        if not fast.next or not fast.next.next:
            return None

        slow2 = head

        while slow.next:
            if slow ==slow2:
                return slow
            slow = slow.next
            slow2 = slow2.next


pos = -1
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
res = (node1.check_cycle(node1))
print(res.val)
res = (node1.detect_cycle(node1))
print(res.val)

    
