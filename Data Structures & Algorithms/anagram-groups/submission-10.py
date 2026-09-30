class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charmap = {}
        
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            if tuple(chars) not in charmap:
                charmap[tuple(chars)] = [s]
            else:
                charmap[tuple(chars)].append(s)
        return [v for v in charmap.values()]