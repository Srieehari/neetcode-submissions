class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        

        stack = []  
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            
            if i < n:
                current_height = heights[i]
            else:
                current_height = 0

            while stack and current_height < heights[stack[-1]]:
                top_index = stack.pop()
                height = heights[top_index]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                area = height * width
                if area > max_area:
                    max_area = area

            stack.append(i)

        return max_area