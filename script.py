### 1.1  Module 1 — Variables et syntaxe
from collections import defaultdict
from copy import deepcopy

nom  =  "Karim"
prenom  =  "Ben  Ali"
notes  =  [12,  15,  9]

somme = 0
nbr_notes = 0
for note in notes:
    somme += note
    nbr_notes +=1

print(f"{nom} moyenne : {somme / nbr_notes:>6.2f}/20")

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

"""
nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")
notes = []

for i in range(3):
    note = input(f"Entrez la note {i + 1} : ")
    
    #what mean this exactement:
    if note.replace(".", "", 1).isdigit():
        note = float(note)
        notes.append(note)
    else:
        print("Erreur : la note doit être un nombre.")
"""

print("\n*************************************************\n")

def calculer_moyenne(notes):
    somme = 0

    #if not notes:
    if len(notes) == 0:
        print("Attention: Aucun note fournie.")
        return 0
    #return sum(notes) / len(notes)
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
    if len(notes) != len(coefficients):
        print("Erreur: Le nombre de notes doit correspondre au nombre de coefficients.")
        return None

    if not notes:
        print("Attention: Aucun note fournie.")
        return 0
    i=0
    total = 0
    coff  =0
    somme_produits = sum(note * coff for note, coff in zip(notes, coefficients))
    somme_coefficients = sum(coefficients)

    if somme_coefficients == 0:
        print("Erreur: La somme des coefficients est zero, impossible de calculer la moyenne pendérée")
        return None

    return somme_produits / somme_coefficients

notes = [14, 10, 18] # Maths, Francais, Sport
coefficients = [3, 2, 1]
moyenne_p = calculer_moyenne_ponderee(notes, coefficients)

if moyenne_p is not None:
    print(f"Moyenne pondérée : {moyenne_p:.2f}/20")


def appreciation(moy):
    #for moy in moyenne:
    if moy < 10:
        print(f"{moy} -> Insuffisant\n")
    elif 10 <= moy < 12:
        print(f"{moy} -> Passable\n")
    elif 12 <= moy < 16:
            print(f"{moy} -> Bien\n")
    else:
        print(f"{moy} -> Tres bien\n")

def appreciation2(moy):
    if moy < 10:
        return "Insuffisant"
    elif 10 <= moy < 12:
        return "Passable"
    elif 12 <= moy < 16:
        return "Bien"
    elif 16 <= moy <= 20:
        return "Tres bien"
    return None

valeurs_test = [9.9, 10.0, 11.9, 12.0, 15.9, 16.0, 20.0]

for valeur in valeurs_test:
    print(f"{valeur:>6.2f} : {appreciation2(valeur)}")

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

    etudiants_trie1 = sorted(copy_etudiants, key=lambda e:e.get("moyenne"))
    print(copy_etudiants)
    #etudiants_trie2 = sorted(etudiants, key=lambda e:e.get("moyenne"))
    print(etudiants)

    print(f"Meilleur  etudiant : {etudiants_trie1[len(etudiants_trie1) -1].get("nom")}")
    print(f"Moins  bon  etudiant : {etudiants_trie1[0].get("nom")}")

"""
meilleure_moyenne = -1
meilleur_etudiant = ""
pire_moyenne = 21
pire_etudiant = ""

for etudiant in etudiants:
    moyenne_etudiant = calculer_moyenne(etudiant['notes'])

    if moyenne_etudiant > meilleure_moyenne:
        meilleure_moyenne = moyenne_etudiant
        meilleur_etudiant = etudiant['nom']

    if moyenne_etudiant < pire_moyenne:
        pire_moyenne = moyenne_etudiant
        pire_etudiant = etudiant['nom']

print(f"Le meilleur étudiant est {meilleur_etudiant} avec une moyenne de {meilleure_moyenne:.2f}/20")
print(f"Le moins bon étudiant est {pire_etudiant} avec une moyenne de {pire_moyenne:.2f}/20")
"""

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

def regrouper_par_montion(resultat):
    dicto = defaultdict(list)
    for cle, valeur in resultat.items():
        print(f"{cle} => {valeur['mention']}")
        dicto[valeur['mention']].append(cle)
    return dict(dicto)


def moyenne_groupe(etudiants):

    if len(etudiants) == 0:
        print("Attention: Aucun etudiant fourni.")
        return 0
    somme_moyenne_general = 0
    nombre_etudiants = 0
    for etudiant in etudiants:
        if etudiant['notes']:
            somme_moyenne_general += calculer_moyenne(etudiant.get('notes'))
            nombre_etudiants += 1

        if nombre_etudiants == 0:
            return 0

    return somme_moyenne_general / nombre_etudiants

etudiants = [
{"nom": "Karim", "notes": [12, 15, 9]},
{"nom": "Sara", "notes": [18, 17, 16]},
{"nom": "L ina", "notes": [6, 8, 5]},
]
moyenne_generale_classe = moyenne_groupe(etudiants)
print(f"La moyenne générale de la classe est : {moyenne_generale_classe:.2f}/20")

def somme_recursive(notes):
    if not notes:
        print("Attention: Aucun note fournie.")
        return 0
    else:
        return notes[0] + somme_recursive(notes[1:])

notes_pour_somme = [12, 15, 9, 18]
resultat_somme = somme_recursive(notes_pour_somme)
print(f"La somme récursive des notes {notes_pour_somme} est : {resultat_somme}")


def a_des_doublants(noms):
    a_des_doublons = len(noms) != len(set(noms))
    #compteur = {x: noms.count(x) for x in set(noms)}
    return  a_des_doublons

def fusionner_dictionnaires(d1, d2):
    copy_d1 = deepcopy(d1)
    for key, value in d2.items():
        if key not in d1:
            copy_d1[key] = value
        else:
            print(copy_d1[key])
            print(copy_d1[key].values())
            copy_d1[key] = [copy_d1[key], value]
            #copy_d1[key].append(value)

    return copy_d1

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

    resultatss = {
        "Karim": {"moyenne": 12.0, "mention": "Bien"},
        "Sara": {"moyenne": 17.0, "mention": "Tres  bien"}, "Lina": {"moyenne": 8.7, "mention": "Insuffisant"},
        "Nadia": {"moyenne": 13.5, "mention": "Bien"},
    }

    print(f"\n{regrouper_par_montion(resultatss)}")

    noms = ["Karim", "Sara", "Lina", "Lina", "Lina", "Lina", "Karim"]
    groupe_a = {
        "Karim": {"moyenne": 12.0, "mention": "Bien"},
    }
    groupe_b = {
        "Karim": {"moyenne": 15.0, "mention": "Bien"},
        "Sara": {"moyenne": 17.0, "mention": "Tres  bien"}, }
    #c = {**groupe_a, **groupe_b}
    print("\n***************\n")
    group_fussion = dict()
    for item in groupe_a:
        if item in groupe_b:
            print("exist")
        else:
            group_fussion = groupe_a | groupe_b
            print(group_fussion)
            #return group_fussion
    #c = groupe_a  groupe_b
    print("\n********\n")
    print(fusionner_dictionnaires(groupe_a, groupe_b))

    #if a_des_doublants(list(c)):
    #    print("Attention, il ya des doublons!")

    print("\n************ Fin Module 3*****************************\n")



if __name__ == '__main__':
    main()
