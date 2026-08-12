class Solution:

    def encode(self, strs: List[str]) -> str:
        w = ""
        for s in strs:
            w += str(len(s)) + "#" + s
        return w          # no trailing separator to strip anymore

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while j < n and s[j] != '#':
                j += 1
            if j == n:
                break
            length = int(s[i:j])
            start = j + 1
            end = start + length      # no -1
            lst.append(s[start:end])
            i = end
        return lst