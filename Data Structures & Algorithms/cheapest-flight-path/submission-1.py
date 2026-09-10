class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):

        arr = [float('inf')] * n
        arr[src] = 0

        for _ in range(k + 1):
            temp = arr[:]

            for f, t, p in flights:
                if arr[f] != float('inf'):
                    temp[t] = min(temp[t], arr[f] + p)

            arr = temp

        return arr[dst] if arr[dst] != float('inf') else -1