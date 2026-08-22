class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        
        k=k%len(nums)
        res=[]
        for j in range(len(nums)-k,len(nums)):
            res.append(nums[j])
        for i in range(len(nums)-k):
            res.append(nums[i])
        nums[:] = res