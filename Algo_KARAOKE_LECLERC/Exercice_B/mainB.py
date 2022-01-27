from playerB import Player
from karaoke import Karaoke


joueur1= Player("Mathieu", [54,96,0,0])
joueur2= Player("Sébastien", [85,50,0,0])
joueur3= Player("Quentin", [92,0,25,0])
karaoke= Karaoke(["Chanson1", "Chanson2", "Chanson3", "Chanson4"],[joueur1, joueur2])

print("Les joueurs suivants participent au karaoke: ", karaoke.getListeJoueurs())
karaoke.addPlayer(joueur3)
karaoke.removePlayer(joueur1)
print("Les joueurs suivants participent au karaoke: ", karaoke.getListeJoueurs())
print("Voici la liste des chansons: ", karaoke.getListeChansons())

print("Le meilleur score pour", karaoke.getSongName(0), "est", karaoke.thisSongsBestScore(0))
print("Le meilleur score toutes chansons confondues est ", karaoke.bestScoreOfAll())
print("Le joueur possédant le meilleur score total est " , karaoke.bestTotalScore())
print("La meilleur moyenne est ", karaoke.bestMoyenne())