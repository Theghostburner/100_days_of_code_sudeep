# 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        totalCount = 0
        curr = head
        while curr != None:
            totalCount += 1
            curr = curr.next
        midValue = math.floor((totalCount/2)+1.0)
        print(midValue)
        curr = head
        currCount = 1
        while currCount < midValue:
            currCount +=1
            curr = curr.next
        return curr