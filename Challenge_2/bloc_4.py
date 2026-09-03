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
   for (k, v) in zip(inv1.items(), inv2.items()):
       #print(k1, v1, k2, v2)
       print(f"{k, v}")
       #result[k1] +=

ventes  =  [
{"produit":  "pommes",  "montant":  120}, {"produit":  "bananes",  "montant":  80}, {"produit":  "pommes",  "montant":  45}, {"produit":  "oranges",  "montant":  60}, {"produit":  "bananes",  "montant":  30},
]
total_produits = totaux_ventes(ventes)
print(f"Total  par  produit  : {dict(total_produits)}")

sorted_total_list = list(sorted(total_produits.items(), key=operator.itemgetter(1), reverse=True))
print(f"Meilleur  produit : {sorted_total_list[0][0]} ({sorted_total_list[0][1]})")
print(sorted_total_list)

inv1  =  {"pommes":  20,  "bananes":  15}
inv2  =  {"bananes":  10,  "kiwis":  5}
print("$$$$$$")
fusionner_inventaires(inv1,inv2)

