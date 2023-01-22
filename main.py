import os
from fonctions import *

print('\nBienvenue sur EJAD Encodage.')
print('Il s\'agit d\'une application qui va encoder vos mots de passe afin de les rendre plus sûrs. \n')

entree = input('Veuillez entrer le mot ou code à encoder : ')

longueur = len(entree)

mot_chiffre = 'E'
mot_chiffre = str(mot_chiffre)

j = 1

# On récupère chaque caractère dans le mot entré et on lui donne sa valeur correspondant dans le tableau
for i in entree:

    # La variable caractere prend les caractères (i) du mot
    caractere = i
    # On le met en chaîne de caractère afin de pouvoir faire la concaténation
    caractere = str(caractere)

    # Verification sur la longueur du mot (savoir s'il est pair ou pas)
    if longueur % 2 == 0:
        # S'il est pair...

        # On vérifie si j est < ou > à la longueur divisée par 2. Cela dans le but de placer @ au milieu du mot

        if j < longueur/2 or j > longueur/2:

            # Si le caractère se trouve dans le tableau, on lui donne sa valeur
            if caractere in tableau:
                caractere = tableau[caractere]
                caractere = str(caractere)
                mot_chiffre += caractere
            else:
                # Sinon on affiche un message à l'utilisateur
                print('Le caractère', caractere, 'ne peut être encoder par notre programme pour le moment')
        else:

            # Si j n'est pas < ou > c.-à-d. = à la moitie de la longueur du mot, on insère @ dans le mot
            if caractere in tableau:
                caractere = tableau[caractere]
                caractere = str(caractere)
                mot_chiffre = mot_chiffre + caractere + '@'
            else:
                print('Le caractère', caractere, 'ne peut être encoder par notre programme pour le moment')
    else:
        # Si la longueur du mot est impair...

        # On cherche alors à savoir si j est <, > ou = à la partie entière de la division de la longueur par 2
        if j < longueur//2 or j > longueur//2:
            # Si j est < ou > à cette partie entière, le cryptage se fait normalement
            if caractere in tableau:
                caractere = tableau[caractere]
                caractere = str(caractere)
                mot_chiffre += caractere
            else:
                print('Le caractère', caractere, 'Ne peut être encoder par notre programme pour le moment')
        else:
            # Si j est = à cette partie entière, après avoir encodé le caractère, on insère & dans le mot
            if caractere in tableau:
                caractere = tableau[caractere]
                caractere = str(caractere)
                mot_chiffre = mot_chiffre + caractere + '&'
            else:
                print('Le caractère', caractere, 'Ne peut être encoder par notre programme pour le moment')

    j += 1

print('\nL\'encodage de \'', entree, '\' par notre programme est : ', mot_chiffre, '\n')


os.system('pause')
