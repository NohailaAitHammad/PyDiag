from _pyrepl import commands
from collections import defaultdict


def vendre(stock, produit, quantite):
    if not stock:
        print("Stock Vide\n")
        return None

    if produit not in stock:
        print("Produit n'extste pas\n")
    else:
        if quantite > stock.get(produit):
            print(f"Stock insuffisant pour {produit} (disponible: {stock.get(produit)})")
        else:
            stock[produit] -= quantite
            print(f"Vente  enregistree  :  {quantite} {produit}.")

    return stock
def produits_epuises(stock):
    return list({k:v for k,v in stock.items() if v == 0})

def total_par_client(commandes):
    resultat = defaultdict(int)

    for commande in commandes:
        resultat[commande['client']] += commande['quantite']
    return resultat

def inverse_dict(a):
    return {v:k for k,v in a.items()}

def dict_len(mots):
    return {mot: len(mot) for mot in mots}

def dict_imbrique(d):
    result= {k: len(v) for k,v in d.items()}
    for k,value in result.items():
        print(f"{k}:{value} employ(e)")

stock  =  {"pommes":  50,  "bananes":  30,  "oranges":  0}
vendre(stock,  "pommes",  20)
vendre(stock,  "oranges",  5)
vendre(stock,  "batata",  5)
stockk = []
vendre(stockk,  "batata",  5)
print("**************")
stock  =  {"pommes":  30,  "bananes":  0,  "oranges":  0,  "kiwis":  12}
print(produits_epuises(stock))
print("**************")

d  =  {"a":  1,  "b":  2,  "c":  3}
print(d)
print(inverse_dict(d))

print("**************")

commandes  =  [
{"client":  "Ali",  "produit":  "pommes",  "quantite":  5}, {"client":  "Sara",  "produit":  "bananes",  "quantite":  10}, {"client":  "Ali",  "produit":  "oranges",  "quantite":  2},
]
print(total_par_client(commandes))

print("**************")

mots  =  ["chat", "elephant",  "abeille",  "riz"]
print(dict_len(mots))

print("**************")

entreprise  =  {
"IT":  ["Ali",  "Sara",  "Omar"],
"RH":  ["Lina"],
"Ventes":  ["Karim",  "Yasmine",  "Nadia",  "Hicham"], }
dict_imbrique(entreprise)


