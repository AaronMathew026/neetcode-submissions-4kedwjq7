class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_length = 0
        hash_map = {}
        for r in range(len(s)):
            if s[r] in hash_map:
                hash_map[s[r]] +=1
            else:
                hash_map[s[r]] = 1
            max_freq = max(hash_map.values())
            swaps = ((r-l+1)-max_freq)
            if swaps <=k:
                max_length = max(max_length, r-l+1)
            else:
                hash_map[s[l]] -=1
                l+=1

        return max_length


        
        