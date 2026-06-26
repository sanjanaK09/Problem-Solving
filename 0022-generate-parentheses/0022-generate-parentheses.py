class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(current_str, left, right):
            if left == 0 and right == 0:
                result.append(current_str)
                return
            if left > 0:
                dfs(current_str + "(", left - 1, right + 1)
            if right > 0:
                dfs(current_str + ")", left, right - 1)
        dfs("", n, 0)
        return result        