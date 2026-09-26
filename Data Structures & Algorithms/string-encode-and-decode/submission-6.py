class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            length = len(s)
            result.append(str(length))
            result.append('#')
            result.append(s)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = s[i:j] #currently i is at 0, get length
            j += 1
            i = j
            j += int(length) # start of str
            result.append(s[i:j])
            i = j
        return result


