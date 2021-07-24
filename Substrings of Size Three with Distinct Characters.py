Runtime: 24 ms, faster than 98.80% of Python3 online submissions for Substrings of Size Three with Distinct Characters.
Memory Usage: 14.3 MB, less than 42.54% of Python3 online submissions for Substrings of Size Three with Distinct Characters.
```
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)-2):
            if(s[i]!=s[i+1] and s[i]!=s[i+2] and s[i+1]!=s[i+2]):
                count+=1
        return count