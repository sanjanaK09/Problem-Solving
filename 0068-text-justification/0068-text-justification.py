class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, i = [], 0
        while i < len(words):
            j, length = i + 1, len(words[i])
            while j < len(words) and length + 1 + len(words[j]) <= maxWidth:
                length += 1 + len(words[j])
                j += 1
            
            line_words = words[i:j]
            gaps = len(line_words) - 1
            
            if j == len(words) or gaps == 0:
                res.append(" ".join(line_words).ljust(maxWidth))
            else:
                spaces = maxWidth - sum(len(w) for w in line_words)
                base, extra = spaces // gaps, spaces % gaps
                for k in range(extra):
                    line_words[k] += " "
                res.append((" " * base).join(line_words))
                
            i = j
        return res
        