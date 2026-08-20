class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m=nums.index(min(nums))
        arr1=nums[:m]
        arr2=nums[m:]
        if target in arr1:
            l,r=0,len(arr1)-1
            res=0
            while l<=r:
                mid=(l+r)//2
                if target>mid:
                    l=mid+1
                elif target<mid:
                    r=mid-1
                else:
                    return mid
        elif target in arr2:
            l,r=0,len(arr1)-1
            res=0
            while l<=r:
                mid=(l+r)//2
                if target>mid:
                    l=mid+1
                elif target<mid:
                    r=mid-1
                else:
                    return mid+len(arr1)-1
        else:
            return -1
        