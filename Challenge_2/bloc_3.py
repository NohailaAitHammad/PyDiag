def union(a,b):
    return set(a).union(set(b))

def intersection(a,b):
    return set(a).intersection(set(b))

def difference(a,b):
    return set(a).difference(set(b))
def a_des_doublant(a):
    x= set(a)
    return True if len(a) != len(x) else False
def set_unique(d):
    s = set()
    #for item in d:
    #    for i in item:
    #        s.add(i)
    #return s 
    return set([x for sous_liste in d for x in sous_liste])


atelier_python = ["Ali", "Sara", "Lina", "Karim"]
atelier_java = ["Sara", "Omar", "Lina", "Yasmine"]
print(f"Inscrits aux deux ateliers: {intersection(atelier_java, atelier_python)}")
print(f"Inscrits a au moins un atelier : {union(atelier_java, atelier_python)}")
print(f"Uniquement Python : {difference(atelier_python, atelier_java)}")

liste_1 = ["Ali", "Sara", "Lina"]
liste_2 = ["Ali", "Sara", "Ali"]
print(a_des_doublant(liste_1))
print(a_des_doublant(liste_2))

tags_articles  =  [
["python",  "web",  "api"], ["python",  "data"],
["web",  "css"], ]
print(set_unique(tags_articles))

"""
les sets store seulement  les elements immutables(hashables) non modifiables comme les nombres les tuples et les strings et non pas les listes et les dictionnaires car il sont mutables
"""
#coordonnees  =  {[1,  2],  [3,  4]}  #  leve  une  TypeError