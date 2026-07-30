class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1
        res = []
        for i in range(n - 1, -1, -1):
            idx = k // math.factorial(i)
            res.append(numbers.pop(idx))
            k %= math.factorial(i)
        return "".join(res)
        