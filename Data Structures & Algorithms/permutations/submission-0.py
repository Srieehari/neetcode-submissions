from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def helper(used):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in nums:
                if i in used:
                    continue
                subset.append(i)
                used.add(i)
                helper(used)
                used.remove(i)
                subset.pop()

        helper(set())
        return res
