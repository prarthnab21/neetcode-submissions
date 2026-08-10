class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                sub1 = (s[left+1 : right+1]) 
                sub2 = (s[left : right])
                if sub1 == sub1[::-1] or sub2 == sub2[::-1]:
                    return True
                else:
                    return False

            left += 1
            right -= 1

        return True