from player import Player

joueur1=Player("Mathieu", [54,50,81,95,0])
print(joueur1.getPseudo())
print(joueur1.getScores())
print(joueur1.scoreTotal())
print(joueur1.moyenne())
print(joueur1.meilleurScore())
print(joueur1.pireScore())
joueur1.newScore(45,4)
print(joueur1.getScores())
