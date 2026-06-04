class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        cleaned = ""
        for i in s:
            if i.isalnum():
                cleaned += i
        r = cleaned[::-1]
        if cleaned == r:
            return True
        else:
            return False
