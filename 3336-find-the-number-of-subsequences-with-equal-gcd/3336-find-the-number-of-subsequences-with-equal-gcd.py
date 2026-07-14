class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        max_num = max(nums)
        
        dp = [[0] * (max_num + 1) for _ in range(max_num + 1)]
        dp[0][0] = 1
        
        for num in nums:
            next_dp = [[0] * (max_num + 1) for _ in range(max_num + 1)]
            for g1 in range(max_num + 1):
                for g2 in range(max_num + 1):
                    if dp[g1][g2] == 0:
                        continue
                        
                    next_dp[g1][g2] = (next_dp[g1][g2] + dp[g1][g2]) % MOD
                    
                    ng1 = math.gcd(g1, num)
                    next_dp[ng1][g2] = (next_dp[ng1][g2] + dp[g1][g2]) % MOD
                    
                    ng2 = math.gcd(g2, num)
                    next_dp[g1][ng2] = (next_dp[g1][ng2] + dp[g1][g2]) % MOD
            dp = next_dp
            
        ans = 0
        for g in range(1, max_num + 1):
            ans = (ans + dp[g][g]) % MOD
            
        return ans
        