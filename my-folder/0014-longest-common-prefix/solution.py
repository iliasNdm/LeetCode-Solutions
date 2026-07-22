class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        min_len = min(len(w) for w in strs)
        for i in range(min_len):
            new_prefix = prefix + strs[0][i]
            if all(word.startswith(new_prefix) for word in strs):
                prefix = new_prefix
            else:
                break
        return prefix

        
