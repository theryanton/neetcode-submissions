class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strmap = {}
        for s in strs:
            if str(sorted(s)) not in strmap:
                strmap[str(sorted(s))] = [s]
            else:
                strmap[str(sorted(s))].append(s)
        
        return [v for v in strmap.values()]