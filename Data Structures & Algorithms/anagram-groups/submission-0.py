class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_freq = {}
        sorted_list = [''.join(sorted(string)) for string in strs]

        for index,string in enumerate(sorted_list):
            if string in string_freq:
                string_freq[string].append(strs[index])
            else:
                string_freq[string] = [strs[index]]
        
        return list(string_freq.values())


