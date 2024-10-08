class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteList = [*ransomNote]
        magazineList = [*magazine]
        
        for i in ransomNoteList:
            if i not in magazineList:
                return False
        
        magazineList = [letter for letter in magazineList if letter in ransomNoteList]

        for j in magazineList:
            if j in ransomNoteList:
                ransomNoteList.remove(j)
        
        if len(ransomNoteList) == 0:
            return True
