class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        


        def merge(interval1, interval2):


            front = max(interval1[0], interval2[0])
            back = min(interval1[1], interval2[1])

            return back-front >= 0

        

        intervals.sort(key=lambda x: x[0] )

        res = [intervals[0]]



        for interval in intervals:

            interval2 = res[-1]


            if merge(interval, interval2):


                a = min(interval[0], interval2[0])
                b = max(interval[-1], interval2[-1])


                res[-1] = [a, b]

            else:

                res.append(interval)


        return res


