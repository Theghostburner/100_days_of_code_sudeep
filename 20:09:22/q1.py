# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        l1 = list1
        l2 = list2
        while l1 != None:
            arr.append(l1.val)
            l1 = l1.next
        while l2 != None:
            arr.append(l2.val)
            l2 = l2.next
        arr.sort()
        head = ListNode()
        curr = ListNode()
        head.next = curr
        curr.val = ""
        for i in range(len(arr)):
            if(i == 0):
                curr.val = arr[0]
                continue
            newNode = ListNode()
            newNode.val = arr[i]
            curr.next = newNode
            curr = newNode
        return head.next
            