#Morpion
#Assigner a Board les valeurs : 1o fois " "
board=[" "," "," "," "," "," "," "," "," "," "]
#assigner a Victoire qui est egqle a 1 
Victoire = 1
#Assigner a Draw qui est egale a -1
Draw = -1
#Assigner a Runnig qui est egale a 0
Running = 0
#assigner a stop qui est egale a 1
Stop = 1
#Assigner a Joueur qui est egale a 1
Joueur = 1 
#Assigner a Game qui est egale a running donc 1
Game = Running    
#Assigner a Signe qui contient le caractere X 
Signe = 'X' 

#Definir une fonction Board sans parametre 
def Board():
    #Afficher mon tableau de jeu 
    print(board[7], " |",board[8],"|",board[9] + "          7 | 8 | 9 ") 
    print("___|___|___"                        + "        ___|___|___")
    print(board[4]," |", board[5],"|",board[6] + "    ex:   4 | 5 | 6 ")
    print("___|___|___"                        + "        ___|___|___")
    print(board[1], " |",board[2],"|",board[3] + "          1 | 2 | 3 ")
    print("   |   |   "                        + "           |   |   ")
 
#Definir une fonction CheckCase avec comme parametre x :
def CheckCase(x):
    #Si Board pour tous x est bien egale ' ' -> caractere vide
    if(board[x] == ' '):
        #Alors je retourne Vrai  
        return True   
    #Sinon 
    else:
        #Alors je retourne Faux   
        return False    
   
#Definir une fonction Victoire sans parametre
def Victoire():
    #Assigner a game un environement global  
    global Game    
    # Condition de Victoire horizontale
    # Si board 1 est bien egale a board 2 et que board 2 est bien egale a board 3 et board 1 est different de ' ' 
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        #Alors assigner a Game qui est egale a Victoire  
        Game = Victoire
    # Sinon si board 4 est bien egale a board 5 et que board 5 est bien egale a board 6 et board 4 est different de ' '  
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Victoire
    # Sinon si board 7 est bien egale a board 8 et que board 8 est bien egale a board 9 et board 7 est different de ' '  
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Victoire    
    # Condition de victoire verticale
    # Sinon si board 1 est bien egale a board 4 et que board 4 est bien egale a board 7 et board 1 est different de ' '    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Victoire   
    # Sinon si board 2 est bien egale a board 5 et que board 5 est bien egale a board 8 et board 2 est different de ' ' 
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Victoire    
    # Sinon si board 3 est bien egale a board 6 et que board 6 est bien egale a board 9 et board 3 est different de ' '
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Victoire 
    #Condition de victoire diagonale 
    # Sinon si board 1 est bien egale a board 5 et que board 5 est bien egale a board 9 et board 5 est different de ' '   
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Victoire    
    # Sinon si board 3 est bien egale a board 5 et que board 5 est bien egale a board 7 et board 5 est different de ' '
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Victoire    
    #Match Condition d'égalité ou de match nul    
    # Sinon si board 1 est different de ' ' et board 2 est different de ' ' et board 3 est different de ' ' et board 4 est different de ' ' ect ....
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        #Alors asiigner a Game qui est egale a Draw   
        Game=Draw
    #sinon   
    else:
        #Alors assigner a Game qui est egale a Running         
        Game=Running    
   
print("Le joueur 1 possede les X et Le joueur 2  possede les O :")
while(Game == Running):   
    Board()    
    if(Joueur % 2 != 0):    
        print("Au tour du joueur 1")    
        Signe = 'X'    
    else:    
        print("Au tour du joueur 2")    
        Signe = 'O'    
    choice = int(input("Choisir un nombre du pave numerique pour choisir l'emplacement de votre signe:"))    
    if(CheckCase(choice)):    
        board[choice] = Signe    
        Joueur+=1    
        Victoire()    
    
Board()    
if(Game==Draw):    
    print("tableau de jeu")    
elif(Game==Victoire):    
    Joueur-=1    
    if(Joueur%2!=0):    
        print("Le joueur 1 gagne")    
    else:    
        print("Le joueur 2 gagne") 

Board()