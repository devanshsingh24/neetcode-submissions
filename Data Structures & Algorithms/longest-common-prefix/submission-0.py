from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as prefix
        prefix = strs[0]
        
        # Compare with each subsequent string
        for i in range(1, len(strs)):
            sl = prefix
            st = strs[i]
            j = 0
            # Compare characters until mismatch
            while j < len(sl) and j < len(st) and sl[j] == st[j]:
                j += 1
            # Update prefix to the matched part
            prefix = sl[:j]
            if not prefix:
                return ""
        
        return prefix     