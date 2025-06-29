class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for el in tokens:
            if el=="+":
                num1= numStack.pop()
                num2= numStack.pop()
                numStack.append(num2+num1)
            elif el=="-":
                num1= numStack.pop()
                num2= numStack.pop()
                numStack.append(num2-num1)
            elif el=="*":
                num1= numStack.pop()
                num2= numStack.pop()
                numStack.append(num2*num1)
            elif el=="/":
                num1= numStack.pop()
                num2= numStack.pop()
                numStack.append(int(num2/num1))
            else:
                numStack.append(int(el))
        return numStack[0]
        

        