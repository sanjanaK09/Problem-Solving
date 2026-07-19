class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def backtrack(start, path, target_left):
            if target_left == 0:
                result.append(list(path))
                return
                
            for i in range(start, len(candidates)):
                if candidates[i] > target_left:
                    break
                    
                path.append(candidates[i])
                backtrack(i, path, target_left - candidates[i])
                path.pop()
                
        backtrack(0, [], target)
        return result
        