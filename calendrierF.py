
""""
premier exoercice du TP1: fonctions
19/09/2023
Justin Biscarat-Aymes

Todo:


"""

M31 = [1,3,5,7,8,10,12]
M30 = [4,6,9,11]

MD= { "Janvier":1 , "Février":2 , "Mars":3 , "Avril":4 , "Mai":5 , "Juin":6 , "Juillet":7 , "Août":8 , "Septembre":9 , "Octobre":10 , "Novembre":11 , "Décembre":12 }

def bioupasbi(Annee):
    """
    On créé une fonction qui permet de savoir si l'année reseignée dans la variable "Annee" est une année bissextile
    Annee: le numéro de l'Année
    """
    strAnnee=str(Annee)
    if Annee%4==0 and strAnnee[2:4]!="00":
        return True
    elif Annee%400==0:
        return True
    else:
        return False

def nbjours(Mois, Annee=1200):
    
    
    """Écrire le programme principal qui propose la saisie d'une date, la valide et affiche le message "date
    Cette fonction revoie le nombre de jour du moi demandé
    pour le moi de fevier, si on oublie de préciser l'année a fonction revoie la valeur pour une année bissextile,
    
    Mois: le nom du moi
    Annee: le numéro de l'Année

    """
    Mois=MD[Mois]

    while Mois not in range(1,13):
        Mois=int(input("mettez un mois correct: "))
    if Mois in M31:
        print("31")
    elif Mois in M30:
        print("30")
    elif bioupasbi(Annee)==True:
        print("29")
    else:
        print('28')
    return

