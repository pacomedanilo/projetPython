#Pierre, Feuille, Ciseaux :

#Depuis random importer randint
#Definir la fonction bot avec comme paramètre choixDuBot
    #Assigner a un tableau les caracteres suivant : "pierre", "feuille", "ciseaux"
    #Assigner une variable selectionDuBot qui permet de choisir aleatoirement un nombre entre (0,2) grace a randint dans le tableau avec l'input
    #Retourner choixDuBot

#Definir la fonction joueur avec comme paramètres choixDuJoueur et n
    #Assigner round egale a 0
    #Assigner pointJoueur egale a 0
    #Assigner pointBot egale a 0
    #Assigner une variable nbRound qui permet de contenir le ne nombre de round avec l'input "Combiien de round?"
    #Tant que le round est inferieur a nbRound
    #Alors j'incremente nbRound + 1
    #Assigner une variable selectionDuJoueur qui permet de contenir le signe avec l'input "Choisir un signe : Pierre Feuille Ciseaux ?"


    #Si le choixDuJoueur est egale a choixDuBot
        #Alors afficher Egalitee   
    #Sinon si choixDuJoueur est egale a pierre et le choixDuBot est egale a feuille
        #Alors afficher le bot gagne
        #Assigner a pointBot egale a pointBot + 1
    #Sinon si choixDuJoueur est egale a pierre et le choixDuBot est egale a ciseaux
        #Alors afficher le joueur gagne
        #Assigner a pointJoueur egale a pointJoueur + 1
    #sinon si choixDuJoueur est egale a feuille et le choixDuBot est egale a pierre
        #Alors afficher le joueur gagne
        #Assigner a pointJoueur egale a pointJoueur + 1
    #sinon si choixDuJoueur est egale a feuille et le choixDuBot est egale a ciseaux
        #Alors afficher le bot gangne
        #Assigner a pointBot egale a pointBot + 1
    #Sinon si choixDuJoueur est egale a ciseaux et le choixDuBot est egale a pierre
        #Alors afficher le bot gangne
        #Assigner a pointBot egale a pointBot + 1
    #Sinon si choixDuJoueur est egale a ciseaux et le choixDuBot est egale a feuille
		#Alors afficher le joueur gagne
        #Assigner a pointJoueur egale a pointJoueur + 1

    

    #Afficher "fin round :" avec le nombre de round
	#Affiche Tu as pointJoueur points
    #Affiche Tu as pointBot points

    #Si pointDuJoueur est superieur a pointDuBot
        #Alors afficher le joueur a gagner 
    #Sinon si pointDuJoueur est inferieur a pointDuBot
        #Alors afficher le bot a gagner
    #Sinon afficher egalitee

    