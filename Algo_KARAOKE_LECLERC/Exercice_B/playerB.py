class Player:
    def __init__(self, pseudo, scores):
        self.__pseudo= pseudo
        self.__scores= scores
    
    def getPseudo(self):
        return self.__pseudo

    def getScores(self):
        return self.__scores

    def getSpecificScore(self,song):
        return self.__scores[song]

    def scoreTotal(self):
        total= 0
        for i in range (len(self.__scores)):
            total= total+self.__scores[i]
        return total

    def moyenne(self):
        moyenne= self.scoreTotal()/len(self.__scores)
        return moyenne

    def meilleurScore(self):
        bestScore=0
        for i in range(len(self.__scores)):
            if self.__scores[i]>self.__scores[bestScore]:
                bestScore=i
        return bestScore

    def pireScore(self):
        worstScore=0
        for i in range(len(self.__scores)):
            if self.__scores[i]<self.__scores[worstScore]:
                worstScore=i
        return worstScore

    def newScore(self, newScore, number):
        if newScore>self.__scores[number]:
            self.__scores[number]= newScore


