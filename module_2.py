from copy import deepcopy
from venv import __main__


def calculer_moyenne(notes):
    somme = 0
    if len(notes) == 0:
        print("Attention: Aucun note fournie.")
        return 0
    for note in notes:
        somme += note

    return somme / len(notes)


def appreciation(moyenne):

    for moy in moyenne:
        if moy < 10:
            print(f"{moy} -> Insuffisant\n")
        elif 10 <= moy < 12:
            print(f"{moy} -> Passable\n")
        elif 12 <= moy < 16:
                print(f"{moy} -> Bien\n")
        else:
            print(f"{moy} -> Tres bien\n")


def appreciation_dict(etudiants):
    copy_etudiants = deepcopy(etudiants)

    for etud in copy_etudiants:
        moy = calculer_moyenne(etud.get('notes'))
        etud['moyenne'] = moy

        if moy < 10:
            print(f"{etud.get('nom')} {moy:<6.2f} Insuffisant\n")
        elif 10 <= moy < 12:
            print(f"{etud.get('nom')} {moy:<6.2f} Passable\n")
        elif 12 <= moy < 16:
            print(f"{etud.get('nom')} {moy:<6.2f} Bien\n")
        else:
            print(f"{etud.get('nom')} {moy:<6.2f} Tres bien\n")

    etudiants_trie = sorted(copy_etudiants, key=lambda e:e.get("moyenne"))
    print(f"Meilleur  etudiant : {etudiants_trie[len(etudiants_trie) -1].get("nom")}")
    print(f"Moins  bon  etudiant : {etudiants_trie[0].get("nom")}")

#"""
#def maximum(etudiants):
#    for i in range(1, len(etudiants)):
#        cle = etudiants[i].get("moyenne")
#        #etud_moyenne_i = calculer_moyenne(etudiants[i].get('notes'))
#        j = i-1
#        etud_moyenne_j = calculer_moyenne(etudiants[j].get('notes'))
#
#        while j>=0 and etud_moyenne_j > etud_moyenne_i:
#            etudiants[j+1] = etudiants[j]
#            j -= 1
#        etudiants[j+1] = cle
#
#    return  etudiants
#
#"""

##Défis supplémentaires

def calculer_moyenne_ponderee(notes,  coefficients):
    #tot = 0
    #total_coficient = 0
    #for i in range(len(notes)):
     #   tot += coefficients[i]*notes[i]
      #  total_coficient += coefficients[i]
    #return tot / total_coficient
    if len(notes) == 0:
        print("Attention: Aucun note fournie.")
        return 0
    i=0
    total = 0
    coff  =0
    while  i < len(notes) and i < len(coefficients):

        total += coefficients[i]*notes[i]
        coff += coefficients[i]
        i += 1

    return total / coff

def moyenne_groupe(etudiants):
    if len(etudiants) == 0:
        print("Attention: Aucun etudiant fourni.")
        return 0
    somme_moyenne_general = 0
    for etudiant in etudiants:
        somme_moyenne_general += calculer_moyenne(etudiant.get('notes'))

    return somme_moyenne_general / len(etudiants)


def somme_recursive(notes):
    if len(notes) == 0:
        print("Attention: Aucun note fournie.")
        return 0
    else:
        return notes[0] + somme_recursive(notes[1:])



def main():
    notes = []
    print(f"calculer_moyenne {calculer_moyenne(notes):<6.1f}")

    valeurs_test =  [12.0,  10.0,  11.9,  12.0,  15.9,  16.0,  20.0]
    appreciation(valeurs_test)

    etudiants  =  [
    {"nom": "Karim", "notes": [12, 15, 9]}, {"nom": "Sara", "notes": [18, 17, 16]}, {"nom": "Lina", "notes": [6, 8, 5]},
    ]
    appreciation_dict(etudiants)

    notess = [14, 10, 18]  # Maths,  Francais,  Sport
    coefficients = [3, 2, 1]
    print(f"Moyenne Penderee : {calculer_moyenne_ponderee(notess, coefficients):>6.2f}")

    etudiantss = [
        {"nom": "Karim", "notes": [12, 15, 9]}, {"nom": "Sara", "notes": [18, 17, 16]},
        {"nom": "Lina", "notes": [6, 8, 5]},
    ]
    print(f" moyenne_groupe: {moyenne_groupe(etudiantss):<6.2f}")

    Notess = [12, 15, 9, 18]
    print(somme_recursive(Notess))



if __name__ == '__main__':
    main()