class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ''.join(filter(str.isalnum, s)).lower()
        l, r = 0, len(newString) - 1

        while l <= r:
            if newString[l] == newString[r]:
                l += 1
                r -= 1
            else:
                return False

        return True