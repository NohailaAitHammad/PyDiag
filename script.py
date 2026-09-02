### 1.1  Module 1 — Variables et syntaxe
from copy import deepcopy

nom  =  "Karim"
prenom  =  "Ben  Ali"
notes  =  [12,  15,  9]

somme = 0

for note in notes:
    somme += note
print(f"{nom} moyenne : {somme / 3:>6.2f}")

#Défis supplémentaires
notesInput = []
nomInput = input("Veuillez saisir votre nom: ")
prenomInput = input("Veuillez saisir votre prenom: ")


while len(notesInput) < 3:
    noteInput = input(f"Veuillez saisir  note: ")
    if not noteInput.isdigit():
        print("Ce  n’est  pas  un  nombre  valide,  reessayez.")
    else:
        print(f"Note  acceptee : {float(noteInput)}")
        notesInput.append(float(noteInput))


print("\n*************************************************\n")

def calculer_moyenne(notes):
    somme = 0
    if len(notes) == 0:
        print("Attention: Aucun note fournie.")
        return 0
    for note in notes:
        somme += note

    return somme / len(notes)

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

def construire_resultats(etudiants):
    if len(etudiants) == 0:
        print("Attention: Aucun etudiant fourni.")
        return {}
    resultas = {}
    for etudiant in etudiants:
        resultas[etudiant.get("nom")] = {
            "moyenne": round(calculer_moyenne(etudiant.get("notes")), 1),
            "mention": appreciation2([calculer_moyenne(etudiant.get("notes"))])
        }
    return resultas

def classer_par_moyenne(resultas):
    classer_par_moyenne_decroissante = sorted(resultas.items(), key=lambda e: e[1].get("moyenne"), reverse=True)
    for i, value in enumerate(classer_par_moyenne_decroissante):
        print(f"{i + 1}. {value[0]} - {value[1].get("moyenne")}")
    # print(tuple(classer_par_moyenne_decroissante[len(classer_par_moyenne_decroissante) - 1]))

def etudiants_en_echec(resultats):
    filtred = dict(filter(lambda item: item[1].get("moyenne") < 10, resultats.items()))
    return list(map(lambda e: (e[0], e[1].get('moyenne')), filtred.items()))

#regrouper_par_mention(resultats) Non implementer

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


def appreciation2(moyenne):
    for moy in moyenne:
        if moy < 10:
            return "Insuffisant"
        elif 10 <= moy < 12:
            return "Passable"
        elif 12 <= moy < 16:
            return "Bien"
        elif 16 <= moy <= 20:
            return "Tres bien"
    return None

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


### 2 Section Bonus — Défis avancés

print("\n*************************************************\n")

# Main

def main():
    print("\n************ Module 2*****************************\n")

    notes = [2,2.8, 9.8]
    print(f"calculer_moyenne {calculer_moyenne(notes):<6.1f}\n")

    valeurs_test =  [12.0,  10.0,  11.9,  12.0,  15.9,  16.0,  20.0]
    appreciation(valeurs_test)

    print("\n")

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
    print(f"Moyenne groupe: {moyenne_groupe(etudiantss):<6.2f}\n")


    Notes = [12, 15, 9, 18]
    print(somme_recursive(Notes))

    print("\n************ Fin Module 2*****************************\n")
    print("\n************ Debut Module 3*****************************\n")

    etudiants = [
        {"nom": "Karim", "notes": [12, 15, 9]}, {"nom": "Sara", "notes": [18, 17, 16]},
        {"nom": "Lina", "notes": [6, 8, 5]},
    ]
    print(f" Resultat construire resultats : {construire_resultats(etudiants)}\n")

    resultats = {
        "Karim": {"moyenne": 12.0, "mention": "Bien"},
        "Sara": {"moyenne": 17.0, "mention": "Tres  bien"}, "Lina": {"moyenne": 8.7, "mention": "Insuffisant"},
    }
    classer_par_moyenne(resultats)

    print(f"\n{etudiants_en_echec(resultats)}\n")

    print("\n************ Fin Module 3*****************************\n")



if __name__ == '__main__':
    main()
