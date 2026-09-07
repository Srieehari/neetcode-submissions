from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()

        res = []


        for i in range(len(nums)):


            while window and nums[window[-1]] < nums[i]:

                window.pop()

            window.append(i)


            if window[0] <= i-k:

                window.popleft()

            if i +1 >= k:

                res.append(nums[window[0]])

        return res

            