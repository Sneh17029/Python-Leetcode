#Runtime: 280 ms, faster than 98.82% of Python3 online submissions for Longest Harmonious Subsequence.
#Memory Usage: 15.8 MB, less than 90.07% of Python3 online submissions for Longest Harmonious Subsequence.

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        s = Counter(nums)
        l = 0
        for i in s:
            if i+1 in s:
                l = max(s[i]+s[i+1],l)
        return l