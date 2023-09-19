""""
TP1:deuxieme exercice : fonction impot
19/09/2023
Justin Biscarat-Aymes
Todo


"""

Seuils=[10255, 26071, 74545, 160336]

def mesImpots(revenu):
    """cette fonction permet de calculer la somme totale que quelqu'un doit payer en fonction de son revenu"""
    
    total=0
    if revenu >= 160336:
        total= (revenu-160336)*0.45
        revenu=160336
    if revenu >= 74546:
        total=total+(revenu-74546)*0.41
        revenu=74545
    if revenu >= 26071:
        total=total+(revenu-26071)*0.30
        revenu=26070
    if revenu >= 10256:
        total=total+ (revenu-10256)*0.11
    
    return total

