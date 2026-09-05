"""
Une exception est une erreur qui se
produit lors de l’exécution du programme
Une erreur de syntaxe est le non-respect des regles syntaxiques qui va bloquer le code à l'execution
l'interipteur python aggise comme un traducteur du language python  au language machine
"""
from Challenge_2.bloc_4 import key

extrait_a  =  "print(’bonjour’" # SyntaxError: '(' was never closed
extrait_b  =  "resultat  =  10  /  0" #ZeroDivisionError: division by zero
extrait_c = "valeurs = [1, 2, 3]\nprint(valeurs[5])" # IndexError: list index out of range

def devision_securusee(a,b):
    try:
        resultat = round(a/b, 1)
        print (resultat)
    except ZeroDivisionError:
        print("Erreur : division par zero imposible")

devision_securusee(10,2)
devision_securusee(0,10)

def convertir_entier(n):
    try:
        resultat = int(n)
        print(resultat)
    except ValueError:
        print(f"Erreur: {n} n'est pas un entier valid")
convertir_entier(42)
convertir_entier("abd")

def acceder_element(liste,  index):
    try:
        print(liste[index])
    except IndexError:
        print(f"Erreur: index {index} hors limites(taille de la liste : {len(liste)}")

notes  =  [12,  15,  9]
acceder_element(notes,  1)
acceder_element(notes,  10)

def acceder_cle(dictionnaire,  cle):
    try:
        print(dictionnaire[cle])
    except KeyError:
        print(f"Erreur : la cle '{cle}' n'existe pas.")

eleve  =  {"nom":  "Sara",  "age":  20}
acceder_cle(eleve,  "nom")
acceder_cle(eleve,  "email")


def traiter_valeur(n):
    try:
        nombre = int(n)
    except ValueError:
        print(f"Erreur : {n} n'est pas convertible")
    else:
        print(f"Conversion reussie : {nombre}")
    finally:
        print("Traitement termine.")

traiter_valeur("8")
traiter_valeur("x")
