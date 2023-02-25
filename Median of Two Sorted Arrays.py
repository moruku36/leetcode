'''
このコードは、二分探索法を使って、二つのソートされた配列の中央値を見つける方法です。
考え方は、両方の配列を二つの半分に分割することで、それぞれの配列の左半分の要素数が、両方の配列の右半分の要素数の合計と等しくなるようにすることです。
そして、それぞれの配列の左半分の最大値と右半分の最小値を比較します。もし、それらがある条件を満たしていれば、その平均値が中央値になります。
そうでなければ、どちら側に大きい要素があるかに応じて、分割を調整します。
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # make sure nums1 is always shorter than nums2
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        # initialize some variables
        m = len(nums1)
        n = len(nums2)
        low = 0
        high = m
        
        # binary search loop
        while low <= high:
            # partition both arrays into two halves
            i = (low + high) // 2 # index for nums1
            j = (m + n + 1) // 2 - i # index for nums2
            
            # get max and min elements for comparison
            maxLeft1 = float('-inf') if i == 0 else nums1[i-1]
            minRight1 = float('inf') if i == m else nums1[i]
            maxLeft2 = float('-inf') if j == 0 else nums2[j-1]
            minRight2 = float('inf') if j == n else nums2[j]
            
            # check if we have found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # odd case: return max of left halves
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                # even case: return average of max of left halves and min of right halves
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            
            # adjust partitions based on comparison results
            elif maxLeft1 > minRight2:
                high = i - 1 # move towards left in nums1
            else:
                low = i + 1 # move towards right in nums1