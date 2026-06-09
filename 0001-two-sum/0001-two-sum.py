class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numI = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numI:
                return [numI[complement], i]
            numI[num] = i
