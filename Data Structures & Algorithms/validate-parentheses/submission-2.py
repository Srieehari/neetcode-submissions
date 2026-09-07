class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2 != 0:
            return False


        stack =[]

        mapping = {')': '(', ']': '[', '}': '{'}

        for i in s:


            if i in mapping:


                if len(stack) == 0:

                    return False
                
                val = stack.pop()

                if mapping[i] != val:

                    return False

            else:

                stack.append(i)

        
        
        return not stack




            


        