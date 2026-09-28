class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """


        found = {}

        for i in range(len(nums)):

            if nums[i] in found:
                if abs(i - found[nums[i]]) <= k:
                    
                    return True
            found[nums[i]] = i 

        return False 