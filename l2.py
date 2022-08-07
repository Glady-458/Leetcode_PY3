# def addTwoNumbers(l1, l2):
#     sum = []
#     if len(l1) != len(l2):
#         dif = len(l1)-len(l2)
#         while(len(l1)!=len(l2)):
#             if len(l1)<len(l2):
#                 l1.append(0)
#             else:
#                 l2.append(0)
#
#     # return len(l1),l1,l2
#     for i,s in enumerate(l1):
#         sum.append(l1[i]+l2[i])
#     c = 0
#     for i,s in enumerate(sum):
#         if s >= int(10):
#             carry = s / 10
#             # print(int(carry))
#             forwd = sum[i+1] + carry
#             sum[i+1] = int(forwd)
#             sum[i] = sum[i]%10
#
#
#     return sum
# print(addTwoNumbers([2,4,3,1],[5,6,4]))
# print(addTwoNumbers([2,4,3],[5,6,4]))
# # print (20%10)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev = rslt = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry %10)
            prev = prev.next
            carry //=10
        return rslt.next
