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

#modes_a_identifier  =  {
#   "r" : "Read-only. Raises I/O error if file doesn't exist.",
#   "r+" : "Read and write. Raises I/O error if the file does not exist.Add content at the end of existing content",
#   "w" : "Read and write, This creates a new file if it doesn’t exist, or overwrites the existing file if it does",
#   "w+" : "This creates a new file if it doesn’t exist, or overwrites the existing file if it does",
#   "a" : "Append-only. Adds data to end. Creates file if it doesn't exist.",
#   "a+" : "Read and append. Pointer at end. Creates file if it doesn't exist.",
#   "x",
#   "rb" : "Read in binary mode. File must exist.",
#   "rb+" : "Read and write in binary mode. File must exist.",
#   "wb" : "Write in binary. Overwrites or creates new.",
#   "wb+" : "Read and write in binary. Overwrites or creates new.",
#   "ab" : "Append in binary. Creates file if not exist.",
#   "ab+" : "Read and append in binary. Creates file if it does not exist.",
#   "x" : "création exclusive est spécifié, cela signifie que ce mode ne créera pas de fichier
#   si le fichier portant le nom spécifié existe déjà, accessible en écriture. ",
#   "x" : "fichier est ouvert à la fois en lecture et en écriture."
#}

