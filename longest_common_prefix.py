class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        first = strs[0]

        for i in range(len(first)):
            for word in strs:
                
                if i >= len(word):
                    return prefix
                
                if first[i] != word[i]:
                    return prefix

            prefix += first[i]
        
        return prefix
    