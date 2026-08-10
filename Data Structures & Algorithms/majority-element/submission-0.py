class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, maxCount = 0, 0
        hashMap = {} #keep track of howmany times something occurs

        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1
            ans = n if hashMap[n] > maxCount else ans
            maxCount = max(hashMap[n], maxCount)
        return ans