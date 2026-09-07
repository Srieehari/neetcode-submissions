class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        operators = "+-*/"


        for i in tokens:


            if i in operators:

                val2 = int(stack.pop())
                val1 = int(stack.pop())


                if i == "+":

                    stack.append(val1+val2)

                elif i == "-":

                    stack.append(val1-val2)

                elif i == "*":

                    stack.append(val1*val2)

                else:

                    stack.append(int(val1/val2))
            else:
                stack.append(i)

        return int(stack.pop())


            
        