class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        def backtrack(start: int,current:list[int]):
            if len(current) == k:
                result.append(list(current))
                return
            for num in range(start, n + 1):
                current.append(num)
                backtrack(num + 1, current)
                current.pop()
        backtrack(1, [])
        return result

