Runtime: 40 ms, faster than 98.84% of Python3 online submissions for Maximum Product of Two Elements in an Array.
Memory Usage: 14.4 MB, less than 11.95% of Python3 online submissions for Maximum Product of Two Elements in an Array.
```
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)