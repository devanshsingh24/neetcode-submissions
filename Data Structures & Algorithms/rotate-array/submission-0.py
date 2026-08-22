class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k=k%len(nums)
        res=[]
        for j in range(len(nums)-k,len(nums)):
            res.append(nums[j])
        for i in range(len(nums)-k):
            res.append(nums[i])
        return res