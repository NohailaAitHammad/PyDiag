def verifier_age(age):
    try:
        if age < 0:
            raise ValueError(f"ValueError : l'age ne peut pas etre negativf {age}")
    except ValueError as e:
        print(e)
    else:
        print(f"Age valide: {age}")

verifier_age(25)
verifier_age(-3)

def traiter_liste_de_valeurs(liste):
    for item in liste:
        if not item.isdigit():
            raise ValueError(f"invalid literal for int() with base 10: {item}")

#try:
#    traiter_liste_de_valeurs(["3",  "9",  "x",  "5"])
#except ValueError:
#    print("Log  :  valeur  invalide,  exception  relancee.")
#    raise

class StockInsuffisantError(Exception):
    pass

def retirer_stock(stock, produit, quantite):
    try:
        if stock[produit] < quantite:
            raise StockInsuffisantError(f'StockInsuffisantError : stock insuffisant pour {produit}\n (demande : {quantite}, disponible : {stock[produit]})')
        else:
            print(f'Retrait effectue : {quantite} {produit}')
    except StockInsuffisantError as e:
        print(e)

stock  =  {"pommes":  20,  "bananes":  4}
retirer_stock(stock,  "pommes",  5)
retirer_stock(stock,  "bananes",  10)