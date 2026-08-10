class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(filter(str.isalnum, s)).lower()
        left, right = 0, len(string) - 1

        while left <= right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True