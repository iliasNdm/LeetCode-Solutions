class Solution(object):
    def groupAnagrams(self, strs):
        anagramMap = defaultdict(list)
        for word in strs:
            cle = "".join(sorted(word))
            anagramMap[cle].append(word)
        return list(anagramMap.values())



        
