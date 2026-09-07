import heapq
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        dic = Counter(hand)
        arr = list(dic.keys())
        heapq.heapify(arr)

        while arr:
            start = arr[0]  # Don't pop yet; make sure group is valid first

            for i in range(groupSize):
                val = start + i

                if dic[val] == 0:
                    return False

                dic[val] -= 1

                # Only pop from heap if the count reaches 0 AND val is at the top
                if dic[val] == 0:
                    if val != arr[0]:
                        return False  # Cannot pop out of order
                    heapq.heappop(arr)

        return True
