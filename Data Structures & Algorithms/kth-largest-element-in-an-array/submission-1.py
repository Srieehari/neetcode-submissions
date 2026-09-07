import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:



        arr = []


        for i in nums:


            heapq.heappush(arr, -(i))


        for _ in range(k-1):


            heapq.heappop(arr)


        return -arr[0]


        


