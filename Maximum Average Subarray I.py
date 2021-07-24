#Runtime: 1160 ms, faster than 91.86% of Python3 online submissions for Maximum Average Subarray I.
#Memory Usage: 25.8 MB, less than 86.58% of Python3 online submissions for Maximum Average Subarray I.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        g=sum(nums[:k])
        m=g
        for i in range(len(nums)-k):
            g=g-nums[i]+nums[i+k]
            m=max(m,g)
        return m/k