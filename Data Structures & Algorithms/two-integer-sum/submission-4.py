class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hash={}
        for  i in range (n):
            remain=target-nums[i]
            if remain in hash:
                return [hash[remain],i]
            
            hash[nums[i]]=i
            
