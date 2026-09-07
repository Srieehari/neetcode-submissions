class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def helper(interval1, interval2):

            front = max(interval1[0], interval2[0])
            back = min(interval1[1], interval2[1])

            return back-front >= 0

        intervals.append(newInterval)

        intervals.sort(key = lambda x: x[0])


        res = [intervals[0]]


        for interval in intervals[1:]:

            interval2 = res[-1]

            if helper(interval, interval2):


                a = min(interval[0], interval2[0])

                b = max(interval[1], interval2[1])

                res[-1] = [a,b]

            else:

                res.append(interval)


        return res








        

       