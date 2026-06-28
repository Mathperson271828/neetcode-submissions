class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] = my_dict[num] + 1
            else:
                my_dict[num] = 1

        start = set()
        for num in my_dict:
            if num-1 not in my_dict:
                start.add(num)
        
        sorted_start = sorted(start)
        seq = {}   
        curr = 0
        for num in my_dict:
            if num not in start:
                seq[curr] = seq[curr] + 1
            else:
                curr = num
                seq[curr] = 1

        m = 0
        for key in seq:
            if (seq[key] > m):
                m = seq[key]
        
        return m