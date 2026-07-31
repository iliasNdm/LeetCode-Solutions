class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        for key , value in ransom_counts.items():
            if value <= magazine_counts[key]:
                continue
            else :
                return False
        return True
        
            

