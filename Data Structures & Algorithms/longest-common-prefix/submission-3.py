class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])
        res = ""

        for i in range(n):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return res

            res += strs[0][i]

        return res