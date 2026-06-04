class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in pairs.values():
                stack.append(char)
            else:
                if char in pairs.keys():
                    if stack == []:
                        return False
                    else: 
                        t = stack.pop()
                        if t != pairs[char]:
                            return False
        if stack == []:
            return True
        else:
            return False