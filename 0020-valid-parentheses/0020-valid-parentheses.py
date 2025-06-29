class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        stack=[]
        for letter in s:
            if letter=="}" and len(stack)!=0 and stack[-1]=="{":
                stack.pop(-1)
            elif letter==")" and len(stack)!=0 and stack[-1]=="(":
                stack.pop(-1)
            elif letter=="]" and len(stack)!=0 and stack[-1]=="[":
                stack.pop(-1)
            elif letter=="[" or letter=="(" or letter=="{":
                stack.append(letter)
            else:
                return False
        if(len(stack)!=0):
            return False
        return True