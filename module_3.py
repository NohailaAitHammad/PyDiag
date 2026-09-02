
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
            return "Insuffisant"
        elif 10 <= moy < 12:
            return "Passable"
        elif 12 <= moy < 16:
            return "Bien"
        elif 16 <= moy <= 20:
            return "Tres bien"
    return None

def construire_resultats(etudiants):
    if len(etudiants) == 0:
        print("Attention: Aucun etudiant fourni.")
        return {}
    resultas = {}
    for etudiant in etudiants:
        resultas[etudiant.get("nom")] = {
            "moyenne" : round(calculer_moyenne(etudiant.get("notes")),1),
            "mention" : appreciation([calculer_moyenne(etudiant.get("notes"))])
        }
    return resultas

def classer_par_moyenne(resultas):
    classer_par_moyenne_decroissante = sorted(resultas.items(), key=lambda e: e[1].get("moyenne") ,reverse=True)
    for i, value in enumerate(classer_par_moyenne_decroissante):
        print(f"{i+1}. {value[0]} - {value[1].get("moyenne")}")
    #print(tuple(classer_par_moyenne_decroissante[len(classer_par_moyenne_decroissante) - 1]))

def etudiants_en_echec(resultats):
    filtred = dict(filter(lambda  item: item[1].get("moyenne") < 10, resultats.items()))
    return list(map(lambda e: (e[0], e[1].get('moyenne')), filtred.items()))

def main():
    etudiants  =  [
    {"nom": "Karim", "notes": [12, 15, 9]}, {"nom": "Sara", "notes": [18, 17, 16]}, {"nom": "Lina", "notes": [6, 8, 5]},
    ]
    print(f" Resulmtat : {construire_resultats(etudiants)}")

    resultats = {
        "Karim": {"moyenne": 12.0, "mention": "Bien"},
        "Sara": {"moyenne": 17.0, "mention": "Tres  bien"}, "Lina": {"moyenne": 8.7, "mention": "Insuffisant"},
    }
    classer_par_moyenne(resultats)
    print(etudiants_en_echec(resultats))

if __name__ == '__main__':
    main()