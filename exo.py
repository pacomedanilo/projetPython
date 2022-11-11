def calculSalairParSeconde(salaireHoraire, heureParJourOuvrable, jourOuvrable):
    #Assigner a salaireAnnuel, le nopbre d'heure travaillées en un an
    salaireAnnuel = salaireHoraire * heureParJourOuvrable * jourOuvrable
    #Calcuer, puis assigner a nombreDeSecondeParAn, le nombre de seconde dans une année non bixetile
    nombreDeSecondeParAn = 60 * 60 * 24 * 365
    #Retourner le salaire Annuel divisé par le nombre de seconde par an 
    return salaireAnnuel / nombreDeSecondeParAn

def calculSalaireNet(salaireBrut,coeff):
    #assigner SalaireNet, SalaireBrut*coeff
    SalaireNet = salaireBrut+
    #return SalaireNet
    return SalaireNet

def withdrawfees(total, percent):
    #Calcul du moment des taxes a retirer :
    fees = total * (percent / 100)
    #Retourner la valeur totale moins les taxes
    return total - fees

def calculSalaireNet(salaireBrut, coeff):
    #Calculer et retourner le Salaire Net a partir du salaire brut
    return withdrawFees(salaireBrut, coeff)



def calculSalaireNet(salaireBrut, public):
    #Calculer et retourner le Salaire Net a partir du salaire brut
    #return withdrawFees ( salaireBrut, coeff )
    #si j'occupe un post de la fonction public
    if public:
    #alors je retourne le salaire brut - 15% de taxes
    return withdrawfees(salaireBrut, 15)
    #Sinon ? C'est que je suis travailleur dans le secteur privé, alors je retourne le salaire burt -23% de douille a l'ancienne
    else:
        return withdrawfees(salaireBrut, 23)


def divide(x, y):
    #impossible car y est egale a 0
    if y == 0:
    #alors renvoyer un message d'erreur
        print("bah alors ?")
        return None
    #sinon
    else:
        return x / y
    #retourner le calcule x / y




#exo
    #Faire un mini jeu qui affiche un meessahe lorsque input renvoie le bon caractere
    #le caractere doit etre parametrable 

n=1
#demande de choisir un caractere au joueur
print("je vais vous demander", n + "lettre")
#tant que caractere n'est pas trouver alors la boucle continue
while x == "a":
    x = input("donnez une lettre :")
#renvois un message pour le bon caractere
    if x == "a": 
        print("tu a gagné")
    else:
        print("essaye encore")
def miniGame(lettreSouhaite)
#je defini une variable caratereAleatoire qui permet de contenir le caracterer générer avec input
caractereAleatoire = input()
#tantque caratere aleatoire est different de la lettre souhaitee
    while caractereAleatoire != lettreSouhaite
    #alors j'attribue a caractereAleatoire, une nouvelle lettre
    caractereAleatoire = input()
#si la lettre souhaitee est egale au caractereAleatoire,
if caractereAleatoire == caractereSouhaite:
    #alors j'affiche un message de victoire
    print('vous avez gagnez')

miniGame('a')







tableau = [3,4,9,6,9,7,12,36,58,10]
#pour la valeur 15 je prends l'index 2
print(tableau[2]) #affiche 15

len(tableau) # renvois la longeur du tableau

prenom "pacome"
nom "danilo"
identite = nom + prenom #retourne "pacomedanilo"
identite = nom + ' ' + prenom #retourne "pacome danilo"
*
integrerValue = 342 #renvoie 342
StringIntegrerValue = str(342) #renvoie "342"
    




#exo1
#Faire une fonction qui concatene 2 chaines de caractere, les séparants par une virgule

debut "bonjour"
fin "ca va ?"

def fonction(debut, fin);
    #Assigner a texte les deux chaine de caracteres
    text = debut + "," + " " + fin 
    #affiche "bonjour, ca va ?"
    print (text)


#exo2
#Faire une fonction qui itere sur tous les indexes  d'un tableau renvoyant une chaine de caractere
#avec l'ensembles des occurences d'un chiffres e.g:

tableau = [Marc, Julien, Mathieu]

def fonction(tableau);
    #afficher Marc 
    print(tableau[0])

#pour tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau, 0) doit renvoyer "0, 4, 7" n'hesitez pas a implenter la premiere fonction 

tableau = [0,1,1,1,0,1,1,0,1]

def occurrences(tableau, a):
    i=0
    for x in tableau:
        if (x == a)
        n = n + 1
        print("n, ")







def miniGame(lettreSouhaite)
#je defini une variable caratereAleatoire qui permet de contenir le caracterer générer avec input
caractereAleatoire = input()
#tantque caratere aleatoire est different de la lettre souhaitee
    while caractereAleatoire != lettreSouhaite
    #alors j'attribue a caractereAleatoire, une nouvelle lettre
    caractereAleatoire = input()
#si la lettre souhaitee est egale au caractereAleatoire,
if caractereAleatoire == caractereSouhaite:
    #alors j'affiche un message de victoire
    print('vous avez gagnez')

miniGame('a')


    tableau = [3,4,9,6,9,7,12,36,58,10]
#pour la valeur 15 je prends l'index 2
print(tableau[2]) #affiche 15

tableau  = [ 3 , 4 , 9 , 6 , 9 , 7 , 12 , 36 , 58 , 10 ]
#pour la valeur 15 je prends l'index 2
print ( tableau [ 2 ]) #affiche 15

len ( tableau ) # renvois la longueur du tableau

prénom " pacôme  "
nom  "danilo"
identite  =  nom  +  prenom  #retourne "pacomedanilo"
identite  =  nom  +  ' '  +  prenom  #retourne "pacome danilo"
*
valeurintegrer  =  342  #renvoie 342
StringIntegrerValue  =  str ( 342 ) #renvoie "342"

#exo1
#Faire une fonction qui concatène 2 chaînes de caractères, les séparants par une virgule
début  =  "Bonjour" "
fin = " ça  va ?"

def  fonction ( text ):
text  =  debut  +  " "  +  ","  +  " "  +  "fin"
imprimer ( texte )

#Définir la fonction concaWithComa qui prend comme paramètre strA ET strB
def  concaWithComa ( strA , strB ):
#assigner a stringifiedStrA le retour de l'exécution de la fonction str avc paramètre strA
stringifiéStrA  =  str ( srtA )
#assigner a strifiedStrA le retour de l'exécution de la fonction str avc comme paramètre strA
stringifiéStrB  =  str ( srtB )
#assigner un chaineResultat la concaténation se stringifiedStrA, de la ", " stringifiedStrB
chaineResultat  =  stringifiedA  +  ", "  +  stringifiedStrB
#Retourner chaineResultat
retour  - + chaineResultat




#exo2
#Faire une fonction qui itère sur tous les index d'un tableau renvoyant une chaine de caractère
#avec l'ensembles des occurrences d'un chiffres ex:
#pour tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau, 0) doit renvoyer "0, 4, 7" n'hésitez pas à implémenter la première fonction

tableau  = [ 0 , 1 , 1 , 1 , 0 , 1 , 1 , 0 , 1 ]
#Définir la fonction findIndexes avec parameters une liste tableau et un x quelconque
def  findIndexes ( tableau , x ):
    #on initialise ia 0
    je  =  0
    #Assigner une ChaineRetourner une chaine vide
    chaineRetour  =  "" 
    #tant que je suis inférieur au retour de l'exécution de la fonction lew avec comme paramètre tableau qui retourne le nombre d'entré dans le tableau
    #on initialise est d'abord un vrai
    estPremier  =  vrai
    tandis que  je  <  len ( tableau ):
    # Alors j'assigne une sélection qu'il doit afficher la valeur de tableau à l'index i
    sélectionné  =  tableau [ je ]
    #si sélectionné est egale hache
    si  sélectionné == x :
        #SI isFirst est vrai
        si  estPremier  =  vrai :
        #alors on assigne a chaineRetour a la valeur de i
        chaineRetour  =  i
        #Changer est d'abord un faux
        isFirt  =  faux
    #Sinon
    sinon :
        #sinon j'assigne a chaineRetour le retour de l'exécution de la fonction concaWithComa avec comme paramètre chaineRetour et i
        chaineRetour  =  concaWithComa ( chaineRetour , i )
        #incremante je
        je  =  je  +  1
    #retourner la chaineRetour
    return  chaineRetour

 #faire une table fibonacci
 #definir la fonction fibonacci avec comme parametre n
 def fibonacci(n):
    #assigner a a egale a 1
    a=1
    #assigner a b egale a 1
    b=1
    #si n est egale a 1
    if n==1:
        #alors afficher 'o'
        print('0')
    #sinon si n est egale a 2
    elif n==2:
        #alors afficher '0','1'
        print('0','1')
    #sinon
    else:
        #alors afficher '0'
        print('0')
        #alors afficher a
        print(a)
        #alors afficher b
        print(b)
        #pour i dans range avec parametre n moins 3
        for i in range(n-3):
            #assigner a total qui est la somme de a et b
            total = a + b
            #assigner la variable b egale a 
            b=a
            #assigner la variable a egale a total
            a= total
            #afficher total
            print(total)
         
fibonacci(8)