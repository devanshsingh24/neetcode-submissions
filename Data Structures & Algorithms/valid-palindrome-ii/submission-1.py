class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower() !=s[r].lower():
                return self.isPalindrome(s,l+1,r) or self.isPalindrome(s,l,r-1)
            l,r=l+1,r-1
        return True
    def alphanum(self,c):
        return (ord('a')<=ord(c)<=ord('z')or
        ord('A')<=ord(c)<=ord('Z')or
        ord('0')<=ord(c)<=ord('9'))
    def isPalindrome(self,s,l,r):
        while l<r:
            if s[l].lower() !=s[r].lower():
                return False
            l,r=l+1,r-1
        return True
         