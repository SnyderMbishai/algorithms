class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1:
            return -1
        scores = [0]*n
        for i,o in trust:
            scores[i-1] -= 1
            scores[o-1] +=1
        for i,score in enumerate(scores):
            if score == n-1:
                return i+1
        return -1