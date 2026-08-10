class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1, pointer2 = 0, 0
        ans = []

        while pointer1 < len(word1) or pointer2 < len(word2):
            if pointer1 < len(word1):
                ans.append(word1[pointer1])
                pointer1 += 1
            if pointer2 < len(word2):
                ans.append(word2[pointer2])
                pointer2 += 1

        return ''.join(ans)