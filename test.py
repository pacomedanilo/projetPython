#Pierre, Feuille, Ciseaux :
from random import randint

#Choix du bot
def  bot ( choixDuBot ):
    tableau = ["pierre", "feuille", "ciseaux"]   
    selectionDuBot  = tableau[randint(0,2)]
#Choix du joueur 
def  joueur ( choixDuJoueur, n ):
    round = 0
    pointJoueur = 0
    pointBot = 0
    nbRound  =  input ( "Combiien de round?" )
    while round  <  nbRound:
    nbRround = round + 1
    selectionDuJoueur = input ( "Choisir un signe : Pierre Feuille Ciseaux ?" )

    #Resultat match
	if(choixDuJoueur == choixDuBot):
	    print('Egalitee')
	elif(choixDuJoueur == 'pierre' and choixDuBot == 'feuille'):
		print('bot gagne !')
		pointBot = pointBot + 1
	elif(choixDuJoueur == 'pierre' and choixDuBot == 'ciseaux'):
		print('Le joueur gagne')
		pointJoueur = pointJoueur + 1
	elif(choixDuJoueur == 'feuille' and choixDuBot == 'pierre'):
		print('Le joueur gagne')
		pointJoueur = pointJoueur + 1
	elif(choixDuJoueur == 'feuille' and choixDuBot == 'ciseaux'):
		print('bot gagne !')
		pointBot = pointBot + 1
	elif(choixDuJoueur == 'ciseaux' and choixDuBot == 'pierre'):
		print('bot gagne !')
		pointBot = pointBot + 1
	elif(choixDuJoueur == 'ciseaux' and choixDuBot == 'feuille'):
        print('Le Joueur gagne !')
		pointJoueur = pointJoueur + 1

    #fin de game
    print ('Fin', " Round :"nbRound)
    print('Tu as ', pointJoueur, ' points')
	print('Bot a ', pointBot, ' points')

    if (pointJoueur > pointBot):
        print("Vous avez gagne") 
    elif (pointJoueur < pointBot):
        print("Le bot a gagner")
    else:
        print("Egalitee")