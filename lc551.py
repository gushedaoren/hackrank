class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A")>1:
            return False
        elif s.count("LLL")>0:
            return False
        else:
            return True
            