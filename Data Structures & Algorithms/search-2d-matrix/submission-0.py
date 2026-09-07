class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        



        start = 0
        finish = len(matrix)-1



        while start <= finish:
            mid = (start + finish) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                st, end = 0, len(matrix[mid]) - 1
                while st <= end:
                    middle = (st + end) // 2
                    if matrix[mid][middle] == target:
                        return True
                    elif matrix[mid][middle] < target:
                        st = middle + 1
                    else:
                        end = middle - 1
                return False  

            elif matrix[mid][0] > target:
                finish = mid - 1
            else:
                start = mid + 1

        return False