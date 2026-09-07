class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_end = 0
        farthest = 0

        for i in range(len(nums) - 1):  # stop before the last index
            farthest = max(farthest, i + nums[i])

            # when we reach the end of the current range (i == curr_end)
            if i == curr_end:
                jumps += 1
                curr_end = farthest  # start new range

        return jumps