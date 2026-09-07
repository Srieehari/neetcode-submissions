import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:



        dic = {}


        for i in tasks:


            dic[i] = dic.get(i, 0) + 1


        lst = [(-value, key) for key, value in dic.items()]


        heapq.heapify(lst)



        time = 0

        pending = deque()



        while lst or pending:

            if lst:
                value, letter = heapq.heappop(lst)


                value += 1



                if value < 0:


                    pending.append((time + n , value , letter))




            if pending and pending[0][0] == time:

                time, value, letter = pending.popleft()


                heapq.heappush(lst, (value, letter))


            time +=1



        return time

        







