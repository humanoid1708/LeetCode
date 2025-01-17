# Definition for singly-linked list.
#class ListNode:
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2
        s = ListNode()
        temp = s.next
        s = s.next
        while p or q:
            if p.val == q.val:
                s = ListNode()
                s.val = p.val
                s = s.next
                s = ListNode()
                s.val = q.val
                s = s.next
                p = p.next
                q = q.next
            elif p.val < q.val:
                s = ListNode()
                s.val = p.val
                s = s.next
                p = p.next
            elif q.val < p.val:
                s = ListNode()
                s.val = q.val
                s = s.next
                q = q.next

        return temp

        