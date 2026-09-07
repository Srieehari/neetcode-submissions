class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        def helper(int1, int2):


            front = max(int1[0], int2[0])
            back = min(int1[-1], int2[-1])


            return back-front > 0


        

       
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        count = 0
        prev_end = intervals[0][1]


        for i in range(1, len(intervals)):

            curr_start = intervals[i][0]


            if prev_end > curr_start:

                count +=1

            else:
                prev_end = intervals[i][1]



        

        return count