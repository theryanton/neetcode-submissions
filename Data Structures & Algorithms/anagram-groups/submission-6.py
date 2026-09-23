class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i, string in enumerate(strs):
            sorted_text = "".join(sorted(string))
            if sorted_text in seen: # anagram exists
                seen[sorted_text].append(string)
            else: # new anagram
                seen[sorted_text] = [string]
        return list(seen.values())
        
