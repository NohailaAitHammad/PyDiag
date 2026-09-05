def ecrire_liste_courses(file, liste):
    f = open(file, "w", encoding="utf-8")
    for item in liste:
        f.write("%s\n" % item)

    f.close()

articles  =  ["pommes",  "lait",  "pain"]
ecrire_liste_courses("courses.txt", articles)

def ajouter_article(chemin, article):
    f = open(chemin, "a", encoding="utf-8")
    f.write(article + '\n')
    f.close()

ajouter_article("courses.txt", "oeuf")

def lire_fichier(chemin):
    f = open(chemin, 'r', encoding='utf-8')
    resultat = f.readlines()
    f.close()
    return resultat

caurses_liste = lire_fichier('courses.txt')
print(caurses_liste)

def compter_lignes(chemin):
    f = open(chemin, 'r', encoding='utf-8')
    resultat = f.readlines()
    print(f"Nombre de lignes : {len(resultat)}")
    f.close()

compter_lignes('courses.txt')

#modes_a_identifier  =  ["r",  "w",  "a",  "x",  "rb",  "r+"]

