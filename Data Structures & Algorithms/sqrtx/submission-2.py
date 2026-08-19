class Solution:
    def mySqrt(self, x: int) -> int:
        r,l=0,x
        while r<l:
            mid=(r+l)//2
            if mid*mid<x:
                r=mid+1
            elif mid*mid>x:
                l=mid-1
            else:
                return mid
        return r