class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while right>left:
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            elif s[right].lower()!=s[left].lower():
                return False
            else:
                left+=1
                right-=1
        return True