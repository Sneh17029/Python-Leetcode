#Runtime: 24 ms, faster than 95.95% of Python3 online submissions for Rectangle Overlap.
#Memory Usage: 14.1 MB, less than 77.08% of Python3 online submissions for Rectangle Overlap.

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]):
            return False

        return not (rec1[2] <= rec2[0] or rec1[3] <= rec2[1] or rec1[0] >= rec2[2] or rec1[1] >= rec2[3])