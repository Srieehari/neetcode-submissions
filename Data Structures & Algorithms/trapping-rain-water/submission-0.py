class Solution:
    def trap(self, height: List[int]) -> int:
        

        if len(height) == 0:

            return 0


        left = 0
        right = len(height)-1


        leftMax= height[left]

        rightMax = height[right]

        rest = 0



        while left < right:


            if leftMax< rightMax:

                left+=1

                leftMax = max(leftMax, height[left])

                rest += leftMax-height[left]

            else:

                right-=1

                rightMax = max(rightMax, height[right])
                rest += rightMax-height[right]


        return rest
                