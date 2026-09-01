def calculer_moyenne(notes):
    somme = 0
    for note in notes:
        somme += note

    return somme / len(notes)


#def appreciation(moyenne):

    for moy in moyenne:
        if moy.isdigit():
            if moy < 10:
                print(f"{moy} -> Insuffisant\n")
            elif 10 <= moy < 12:
                print(f"{moy} -> Passable\n")
            elif 12 <= moy < 16:
                    print(f"{moy} -> Bien\n")
            else:
                print(f"{moy} -> Tres bien\n")

            print("no dict")

valeurs_test  =  [{"nom":22},  10.0,  11.9,  12.0,  15.9,  16.0,  20.0]
#appreciation(valeurs_test)


def appreciation_dict(etudiants):
    for etud in etudiants:
        moy = calculer_moyenne(etud.get('notes'))
        if moy < 10:
            print(f"{etud.get('nom')} {moy}  Insuffisant\n")
        elif 10 <= moy < 12:
            print(f"{etud.get('nom')} {moy}Passable\n")
        elif 12 <= moy < 16:
            print(f"{etud.get('nom')} {moy}Bien\n")
        else:
            print(f"{etud.get('nom')} {moy}Tres bien\n")


def maximum(etudiants):
    for i in range(1, len(etudiants)):
        etud_moyenne_i = calculer_moyenne(etudiants[i].get('notes'))
        j = i-1
        etud_moyenne_j = calculer_moyenne(etudiants[j].get('notes'))

        while j>=0 and etud_moyenne_j > etud_moyenne_i:
            etudiants[j+1] = etudiants[j]
            j-=1
        etudiants[j+1] = etudiants[i]
    return  etudiants


etudiants  =  [
{"nom": "Karim", "notes": [12, 15, 9]}, {"nom": "Sara", "notes": [18, 17, 16]}, {"nom": "Lina", "notes": [6, 8, 5]},
]
print(maximum(etudiants))