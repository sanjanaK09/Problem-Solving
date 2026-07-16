class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or len(s) < len(words) * len(words[0]):
            return []
            
        n, m, k = len(s), len(words), len(words[0])
        word_counts, result = Counter(words), []
        
        for i in range(k):
            left = right = i
            curr_counts = Counter()
            count = 0
            
            while right + k <= n:
                word = s[right:right + k]
                right += k
                
                if word in word_counts:
                    curr_counts[word] += 1
                    count += 1
                    
                    while curr_counts[word] > word_counts[word]:
                        curr_counts[s[left:left + k]] -= 1
                        count -= 1
                        left += k
                    
                    if count == m:
                        result.append(left)
                else:
                    curr_counts.clear()
                    count = 0
                    left = right
                    
        return result
            