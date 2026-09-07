class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        


        A, B = nums1, nums2


        if len(B) < len(A):

            A,B = B,A


        tot = len(A)+len(B)

        half = tot//2


        l,r = 0, len(A)


        while l<=r:

            #now that we have the middle number
            i = (l+r)//2

            print(i)
            j = half-i


            Aleft = A[i-1] if i > 0 else float('-inf')
            Aright= A[i] if i < len(A) else float('inf')

            Bleft = B[j-1] if j > 0 else float('-inf')

            Bright= B[j] if j < len(B) else float('inf')



            if Aleft <= Bright and Aright >= Bleft:

                if tot%2 ==0:

                    return (max(Aleft, Bleft) + min(Bright, Aright))/2.0

                else:

                    return float(min(Bright, Aright))

            elif Aleft > Bright:

                r = i - 1

            else:

                l = i + 1

