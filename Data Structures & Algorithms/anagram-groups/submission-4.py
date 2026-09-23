class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            if tuple(count) not in result: # new anagram
                result[tuple(count)] = [string]
            else: # combo already exists
                result[tuple(count)].append(string)
        returned_list = []
        for v in result.values():
            returned_list.append(v)
        return returned_list
        