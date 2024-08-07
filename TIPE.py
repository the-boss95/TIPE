#Partie jeu du taquin

# 1_Affichage d'une position de manière plus lisible

def affiche(chaine) :
    '''Affiche une situation donnée'''
    s='|'
    print (' '+'---'+' ')
    for i in range (len(chaine)):
        s+= chaine[i]
        if (i+1) %3==0:
            print (s+'|')
            s='|'
    print (' '+'---'+' ')
    print ()

exemple_1= '12345678 '
exemple_2= '5216 8473'

# 2_Déterminer la position du vide (compris entre 0 et 8)

def position_elem (chaine, elem):
    '''Renvoie l’indice de la case passer en argument'''
    for i in range (len(chaine)):
        if chaine[i]==elem:
            return i

def position_vide(chaine) :
   '''Renvoie l’indice de la case vide dans une situation'''
    return position_elem (chaine,' ')
    
# 3_Fonction qui intervertit 2 cases (déplacement du vide)

def intervertit (chaine, i, j) :
    '''Intervertit les éléments aux position i et j de la chaine de caractère'''
    if i<j:
        return chaine [: i] +chaine [ j] +chaine [i+1: j] + chaine[i]+chaine[j+1:]
    else:
        return chaine [: j] + chaine[i]+chaine [j+1: i] + chaine[j]+chaine[i+1:]

# 4_Ensemble des nouvelles situations possibles après un coup (dépend de la position du vide)

def positions_voisines (chaine) :
    n= int (len(chaine))
    l= []
    i=position_vide(chaine)
    if i>=3 :              #le vide peut aller vers le haut
        l.append (intervertit (chaine, i, i-3))
    if i<6 :               #le vide peut aller vers le bas
        l.append (intervertit (chaine, i, i+3))
    if i%3>=1 :       #le vide étant sur la colonne du milieu ou de droite gauche, peut aller vers la gauche
        l.append (intervertit (chaine, i, i-1))
    if i%3<=1 :         #le vide étant sur la colonne du milieu ou de gauche, peut aller vers la droite
        l.append (intervertit (chaine, i, i+1))
    return l

# 5_Déterminer si une situation donnée est résoluble

# 5.1_Degré du mélange
    
def degré(chaine):
    chaine=chaine.replace (" ","")
    D=0
    for i in chaine:
        for j in range (len(chaine)):
            if int(i)! = int(chaine[j]):
                if int(i)>int(chaine[j]) and position_elem (chaine, i) <j:
                    D+=1
    return D

# 5.2_solution envisageable ?

def solvable(chaine):
    if degre(chaine)%2==0:
        return True
    else :
        return False

# 6_Parcours de graphe
