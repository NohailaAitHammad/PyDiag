import operator
from collections import defaultdict


def totaux_ventes(ventes):
    #v = defaultdict(int)
    v = defaultdict(int)

    for vente in ventes:
        v[vente['produit']] += vente['montant']
    return v

def produit_distincts(ventes):
    r = set()
    for item in ventes:
        print(item['produit'])
        r.add(item['produit'])
    return r


def fusionner_inventaires(inv1, inv2):

   result = defaultdict(int)

   for d in (inv1, inv2):
       for key, value in d.items():
           result[key] += value

   return dict(result)

def moyenne(matieres):
    somme = 0
    count = 0
    for key, value in matieres.items():
      somme += value
      count += 1

    return somme / count

def moyenne_par_etudiant(etudiants):
    for etudiant in etudiants:
        print(f"{etudiant["nom"]} : {moyenne(etudiant['matieres']):6.2f}")


def metiers_enseignes(etudiants):
    metiers = []

    for etudiant in etudiants:
        metiers.extend(list(etudiant['matieres'].keys()))
        #print(list(etudiant['matieres'].keys()))

    return set(metiers)

def notes_par_matiers(etudiants):
    notes = defaultdict(list)

    for etudiant in etudiants:
        for key, value in etudiant['matieres'].items():
            notes[key].append(value)

    return dict(notes)

def meilleur_metier(r):
    moy = dict()
    for key, value in r.items():
        moy[key] = round(sum(value) / len(value), 2)

    meilleur_matiere = max(moy.items(), key=lambda  item: item[1])
    print(f"Meilleure  matiere  (moyenne  globale)  : {meilleur_matiere[0]} : ({meilleur_matiere[1]})")


ventes  =  [
{"produit":  "pommes",  "montant":  120}, {"produit":  "bananes",  "montant":  80}, {"produit":  "pommes",  "montant":  45}, {"produit":  "oranges",  "montant":  60}, {"produit":  "bananes",  "montant":  30},
]
total_produits = totaux_ventes(ventes)
print(f"Total  par  produit  : {dict(total_produits)}")

sorted_total_list = list(sorted(total_produits.items(), key=operator.itemgetter(1), reverse=True))
print(f"Meilleur  produit : {sorted_total_list[0][0]} ({sorted_total_list[0][1]})")
print(dict(sorted_total_list))

inv1  =  {"pommes":  20,  "bananes":  15}
inv2  =  {"bananes":  10,  "kiwis":  5}

print(fusionner_inventaires(inv1,inv2))

etudiants  =  [
{"nom":  "Ali",  "matieres":  {"maths":  14,  "physique":  12}},
{"nom":  "Sara",  "matieres":  {"maths":  18,  "physique":  16,  "svt":  15}}, {"nom":  "Lina",  "matieres":  {"maths":  9,  "physique":  11}},
]
moyenne_par_etudiant(etudiants)
print(f"Matieres enseignees (set): {metiers_enseignes(etudiants)}")

print("notes  par  matiere  :")
for key, value in notes_par_matiers(etudiants).items():
    print(f"{key} : {value}")

resultat = notes_par_matiers(etudiants)

meilleur_metier(resultat)