class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        entire_product = 1
        zeroes = 0
        for num in nums:
            if (num != 0): 
                entire_product = entire_product * num
            else:
                zeroes = zeroes + 1

        output = []
        if (zeroes > 1):
            for num in nums:
                output.append(0)
        elif (zeroes == 1):
            for num in nums:
                if (num == 0):
                    output.append(entire_product)
                else:
                    output.append(0)
        else:
            for num in nums:
                curr = entire_product//num
                output.append(curr)

        return output