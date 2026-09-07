from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()   # stores indices, not values
        res = []

        for r in range(len(nums)):
            # Pop smaller values from the back
            while window and nums[window[-1]] < nums[r]:
                window.pop()

            window.append(r)

            # Pop from the front if it's out of the window
            if window[0] <= r - k:
                window.popleft()

            # Append the maximum once we have a full window
            if r + 1 >= k:
                res.append(nums[window[0]])

        return res
