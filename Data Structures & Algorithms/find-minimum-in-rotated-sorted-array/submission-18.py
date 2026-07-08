class Solution:
    def findMin(self, nums: List[int]) -> int:
        a = 0
        b = len(nums)-1

        guess = 0

        if (b > 1):
            while (a <= b):
                guess = (a+b)//2

                if (a == b):
                    if (a == len(nums)-1 and nums[0] < nums[a]):
                        guess = 0
                    break

                if (nums[0] > nums[guess]):
                    b = guess
                else:
                    a = guess+1
        else:
            if (b == 1):
                if (nums[0] > nums[1]):
                    guess = 1

        return nums[guess]