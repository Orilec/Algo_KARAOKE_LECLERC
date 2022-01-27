from playerB import Player

class Karaoke:
    def __init__(self, songs, players):
        self.__chansons= songs
        self.__joueurs= players

    def getListeChansons(self):
        return self.__chansons

    def getListeJoueurs(self):
        return self.__joueurs
    
    def getSongName(self, song):
        return self.__chansons[song]

    def addPlayer(self, player):
        self.__joueurs.append(player)

    def removePlayer(self, player):
        if len(self.__joueurs)>1:
            self.__joueurs.remove(player)
    
    def thisSongsBestScore(self, song):
        indexBestScore=0
        bestScore=0
        for i in range(len(self.__joueurs)):
            if (self.__joueurs[i].getSpecificScore(song))>(self.__joueurs[indexBestScore].getSpecificScore(song)):
                indexBestScore=i

        bestScore= self.__joueurs[indexBestScore].getSpecificScore(song)        
        return bestScore

    def bestTotalScore(self):
        bestTotalScore=0
        for i in range(len(self.__joueurs)):
            if (self.__joueurs[i].scoreTotal())>(self.__joueurs[bestTotalScore].scoreTotal()):
                bestTotalScore=i
        
        return self.__joueurs[bestTotalScore].getPseudo()
    
    def bestScoreOfAll(self):
        bestScore=0
        for i in range(len(self.__chansons)):
            if self.thisSongsBestScore(i)>bestScore:
                bestScore= self.thisSongsBestScore(i)
        return bestScore

    def bestMoyenne(self):
        bestMoyenne=0
        for i in range(len(self.__joueurs)):
            if (self.__joueurs[i].moyenne())>bestMoyenne:
                bestMoyenne=self.__joueurs[i].moyenne()
        return bestMoyenne
    

