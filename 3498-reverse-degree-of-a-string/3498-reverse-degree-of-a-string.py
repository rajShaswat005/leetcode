class Solution:
    def reverseDegree(self, s: str) -> int:
        total_sum = 0
        for i, c in enumerate(s):
            rev_val = 26 - (ord(c) - ord('a'))
            pos = i + 1

            total_sum += rev_val * pos
        return total_sum

        
        