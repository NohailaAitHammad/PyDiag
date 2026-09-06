import csv
from itertools import zip_longest
from bloc_2 import StockInsuffisantError

def lire_fichier_securise(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            print(f.readlines())
    except FileNotFoundError:
        print(f"Erreur : le fichier {chemin} n'existe pas.")


lire_fichier_securise('courses.txt')
lire_fichier_securise('inexistant.txt')

def calculer_moyenne_csv(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            data  = csv.reader(f, delimiter=';')
            d = list(data)
            for i in range(1, len(d)):
                if not (d[i][0].split(',')[1]).isdigit() :
                    print(d[i][0].replace(",", "", 1).isdigit())
                #if not (d[i][0].replace(",", "", 1)).isdigit():
                    raise ValueError(f"Attention : note invalid pour '{d[i][0].split(',')[0]}' ('{d[i][0].split(',')[1]}'), ligne ignoree")
    except FileNotFoundError:
        print(f"Erreur : le fichier {chemin} n'existe pas.")
    except ValueError as e:
        print(e)
        notes = []
        for i in range(1, len(d)):
            if d[i][0].split(',')[1].isdigit():
                notes.append(float(d[i][0].split(',')[1]))
            else:
                continue

        print(f" Moyenne calculee  ({len(notes)} notes valides) {round(sum(notes) / len(notes), 2)}")

calculer_moyenne_csv('notes.csv')

def traiter_journal_commandes(stock, commandes, chemain):
    with open(chemain, 'w', encoding="utf-8") as f:
        for commande in commandes:
            produit, quantite_brute = commande.split(',', 1)

            try:
                quantite = int(quantite_brute)

                if produit not in stock:
                    raise KeyError(produit)

                if quantite > stock[produit]:
                    raise StockInsuffisantError(f"stock insuffisant (demande {quantite}, dispo {stock[produit]})")

                stock[produit] -= quantite

                message = f"[OK] {produit} : -{quantite} (reste {stock[produit]})"

            except ValueError:
                message = f"[ERREUR] {produit} : quantite invalide ({quantite_brute})"
            except KeyError:
                message = f"[ERREUR] {produit} : produit inconnu"
            except StockInsuffisantError as e:
                message = f"[ERREUR] {produit} : {e}"

            f.write(message + "\n")

    print("\n--- CONTENU DU JOURNAL ---")
    with open(chemain, "r", encoding="utf-8") as f:
        print(f.read())


stock = {"pommes": 20, "bananes": 4, "oranges": 15}
commandes_brutes  =  [ "pommes,5",
"bananes,10", "kiwis,2",
"oranges,abc", "oranges,5",
]
traiter_journal_commandes(stock, commandes_brutes, 'journal.txt')



