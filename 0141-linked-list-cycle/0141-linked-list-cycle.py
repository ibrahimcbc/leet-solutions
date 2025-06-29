# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr={}
        if not head:
            return False

        while head.next:
            if head in arr:
                return True
            arr[head]=0
            head=head.next
        return False
        