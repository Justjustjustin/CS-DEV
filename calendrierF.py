
""""
premier exoercice du TP1: fonctions
19/09/2023
Justin Biscarat-Aymes

Todo:


"""

M31 = [1,3,5,7,8,10,12]
M30 = [4,6,9,11]

MD= { 1: "Janvier", 2:"Février",3 :"Mars" , 4:"Avril" , 5:"Mai" , 6: "Juin", 7:"Juillet" , 8:"Août" , 9:"Septembre" , 10: "Octobre", 11 :"Novembre" , 12:"Décembre" }

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
    #Mois=MD[Mois]

    while Mois not in range(1,13):
        Mois=int(input("mettez un mois correct: "))
    if Mois in M31:
        return 31
    elif Mois in M30:
        return 30
    elif bioupasbi(Annee)==True:
        return 29
    else:
        return 28
    

def Sdate ():
    """
    cette fonction demande la date, verifie sa validité et l'affiche
    """
    date= input("saisissez la date sous la forme JJ/MM/AAAA: ")
    J,M,A= date.split("/")
    J,M,A=int(J),int(M),int(A)
    
    testAnnee=bioupasbi(A)
    nbJ=nbjours(M,A)

    if J in range(1,nbJ+1) and M in range(1,13):
        return "le "+str(J)+" "+MD[M]+" "+str(A)
    else:
        return False
    
    
    