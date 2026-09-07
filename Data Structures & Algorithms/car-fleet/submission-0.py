class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        '''
            so we have a for loop that goes for i cars


        we go into the for loop and we check the position and speed 

        if the speed is greater than the value in the stack we 

        '''

        pair = [[p,s] for p, s in zip(position, speed)]


        stack = []
        count = 0


        for p,s in sorted(pair)[::-1]:


            stack.append((target-p)/s)


            if len(stack) >= 2 and stack[-1] <= stack[-2]:


                stack.pop()

        return len(stack)

            


           

                

                    
                    
                




        