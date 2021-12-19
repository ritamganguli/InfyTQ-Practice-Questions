class Solution(object):
    def finalValueAfterOperations(self, operations):
        i=0
        s=0
        while(i<len(operations)):
            if operations[i]=="--X":
                s=s-1
            if operations[i]=="X++":
                s=s+1
            if operations[i]=="X--":
                s=s-1
            if operations[i]=="++X":
                s=s+1
            i+=1
        return s
        
