class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        l=0
        maxf=0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]]=1
            else:
                count[s[r]]+=1
            m=max(count,key=count.get)
            m1=count[m]
            maxf=m1+k
        return maxf