class Solution:
    def isPalindrome(self, s: str) -> bool:
        remove_chars = "? !"
        table = str.maketrans("", "", remove_chars)
        cleaned = s.translate(table)
        t=cleaned.lower()
        nwstr=cleaned[::-1]
        p=nwstr.lower()
        
        if t == p:
            return True
        else:
            return False
        
