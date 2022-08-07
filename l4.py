class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a1 = nums1
        a2 = nums2
        r = a1 + a2
        sum = 0
        for n in r:
            sum = sum + n

        return sum/len(r)
c = [1,3] + [2] 
d = 0
for n in c:
    d = d + n
resuld = d/len(c)
print(resuld)     