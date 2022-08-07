class Solution:
    def isPalindrome(self, x: int) -> bool:
        og = x
        temp1 = og
        temp2 = True
        rev = 0
        if temp1 < 0:
            return False
        else:
            while (temp1>0):
                dig = temp1%10
                rev = rev*10+dig
                temp1 = temp1//10
            if og == rev:
                return True
            else:
                return False
