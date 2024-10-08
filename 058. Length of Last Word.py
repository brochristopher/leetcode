class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        myList = s.split(" ")
        print(myList)
        for i in range (len(myList)):
            for j in myList:
                if len(j) < 1:
                    myList.remove(j)
                    print (myList)


        return(len(myList[-1]))
