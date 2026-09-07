class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, arr):
            if len(arr) == k:
                res.append(arr[:])   # copy
                return

            for num in range(i + 1, n + 1):
                arr.append(num)
                dfs(num, arr)
                arr.pop()

        dfs(0, [])
        return res
