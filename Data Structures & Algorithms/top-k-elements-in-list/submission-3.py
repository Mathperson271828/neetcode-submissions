class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] = freq[num] + 1

        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        for i, key in enumerate(sorted_freq):
            if i < k:
                ans.append(key)

        return ans