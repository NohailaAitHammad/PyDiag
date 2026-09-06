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

def journal_commandes(stock, commandes, chemain):
    try:
        with open(chemain, "w+", encoding="utf-8") as f:
            for key, value in stock.items():
                f.write(str(key) +"," + str(value) + '\n')
            f.seek(0)

        with open(chemain, 'a+', encoding="utf-8") as f:
            f.seek(0)
            stock_liste = f.readlines()
            print(stock_liste)
            for commande,item in zip_longest(commandes, stock_liste):
                #print(commande.split(",", 1)[0] in stock_liste)
                if item is not None and commande is not None:
                    if commande.split(",", 1)[0] in item:
                        if item.split(',', 1)[1].replace('\n', '', 1).isdigit():
                            quantite = int(item.split(',', 1)[1].replace('\n', '', 1))
                            #print(f"QUANBTITE{commande.split(",", 1)[1].replace('\n', '', 1)}")
                            if commande.split(",", 1)[1].replace('\n', '', 1).isdigit():
                                if quantite < int(commande.split(",", 1)[1]):
                                    print(f"[ERREUR] stock insuffisant pour {commande.split(",", 1)[0]}")
                                else:
                                    new_value = commande.split(",", 1)[0] + ',' + str(quantite-int(commande.split(",", 1)[1])) + '\n'
                                    idx = stock_liste.index(item)
                                    stock_liste[idx] = new_value
                                    print(f"[OK] {commande.split(",", 1)[0]} : -{commande.split(",", 1)[1]} (reste {str(quantite-int(commande.split(",", 1)[1]))}) ")
                            else:
                                print(f"[ERREUR] quantite  invalide: {commande.split(",", 1)[1]}")
                        else:
                            print(f"[ERREUR] quantite  invalide: {item.split(",", 1)[1]}")
                    else:
                        print(f"[ERREUR] {commande.split(",", 1)[0]} : produit inconnu")

            print(stock_liste)
    except FileNotFoundError:
        print('File not found')
    #except StockInsuffisantError as e:
    #    print(e)


stock = {"pommes": 20, "bananes": 4, "oranges": 15}
commandes_brutes  =  [ "pommes,5",
"bananes,10", "kiwis,2",
"oranges,abc", "oranges,5",
]
journal_commandes(stock, commandes_brutes, 'journal.txt')



