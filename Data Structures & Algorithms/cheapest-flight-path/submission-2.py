class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        arr = [float('inf')] * n
        arr[src] = 0

        for i in range(k + 1):
            temp = arr[:]

            for s, d, p in flights:
                if arr[s] != float('inf'):
                    temp[d] = min(temp[d], p + arr[s])

            arr = temp

        return arr[dst] if arr[dst] != float('inf') else -1