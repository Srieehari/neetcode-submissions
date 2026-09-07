class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        '''
            go for loop with i that goes through entire temperatures 

            what if we put everything into a stack and if the next value is greater than it then we pop the current value and then append the new value 


        '''

        stack = []

        lst = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):


            

            while len(stack) != 0 and temperatures[stack[-1]] < temp:

                j = stack.pop()

                lst[j] = i-j

                
                
            stack.append(i)


        return lst
                




