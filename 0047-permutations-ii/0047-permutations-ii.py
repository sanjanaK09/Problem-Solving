class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)
        nums.sort()
        
        def backtrack(path: list[int]):
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                path.append(num)
                
                backtrack(path)
                
                path.pop()
                used[i] = False
                
        backtrack([])
        return ans
        