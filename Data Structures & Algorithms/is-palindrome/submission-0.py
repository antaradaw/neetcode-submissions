class Solution:
    def isPalindrome(self, s: str) -> bool:
        w=''
        for c in s:
            if (c>='a' and c<='z') or (c>='A' and c<='Z') or (c>='0' and c<='9'):
                w+=c
        w=w.lower()
        return w==w[::-1]
