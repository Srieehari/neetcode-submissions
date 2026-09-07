import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new = []
        for i in stones:
            heapq.heappush(new, -i)  # max-heap via negation

        while len(new) > 1:
            val1 = -heapq.heappop(new)
            val2 = -heapq.heappop(new)

            if val1 != val2:
                heapq.heappush(new, -(val1 - val2))

        return -new[0] if new else 0
