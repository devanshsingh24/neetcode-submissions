class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num3=nums1[:m]
        idx=0
        i,j=0,0
        while idx<m+n:
            if j>=n or (i<m and num3[i]<=nums2[j]):
                nums1[idx]=num3[i]
                i+=1
            else :
                nums1[idx]=nums2[j]
                j+=1
            idx+=1