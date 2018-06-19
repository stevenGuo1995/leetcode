"""
题目：83.删除排序链表中的重复元素

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c = ListNode(0)
        c.next = head.next
        if c.val == c.next.val:
            c.next = c.next.next
        return head.next




# if __name__ == "__main__":
    # node1 = ListNode(1)
    # node2 = ListNode(2)
    # node1.next = node2
    # # s = Solution()
    # # r = s.deleteDuplicates(node1)
    # print(node1.next.val)