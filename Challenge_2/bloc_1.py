from collections import defaultdict


def tri_a_bull(table):
    n = len(table)

    for i in range(n):
        for j in range(n - i -1):
            if table[j] > table[j+1]:
                table[j], table[j+1] = table[j+1], table[j]
    return table


def notes_au_dessus(table, seuil):

    return [n for n in table if n> seuil]

def count_nombre_occurence(table):
    return {x: table.count(x) for x in set(table)}
def reverse_liste(table):
    milieu = len(table)//2
    for i in range(milieu):
        table[i],table[len(table) - i - 1] = table[len(table) - i - 1], table[i]

    return table

def fussion_liste(a, b):
    a.extend(b)
    return tri_a_bull(a)
def caree_nombre_pair(liste):
    return [x**2 for x in liste if x%2 == 0]

def main():
    notes = [12, 18, 7, 15, 9, 20, 3, 14]
    #print(tri_a_bull(notes))
    minimum= tri_a_bull(notes)[0]
    maximun = tri_a_bull(notes)[len(notes) -1]

    print(f"note max : {maximun},\nnote min: {minimum}\n")

    notes = [8, 14, 6, 17, 11, 20]
    seuil = 12
    print(notes_au_dessus(notes, seuil))

    fruits = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]
    print(count_nombre_occurence(fruits))
    liste = [1, 2, 3, 4, 5]
    print(f"Liste avant reverse : {liste}\n")
    print(f"liste apres reverse: {reverse_liste(liste)}\n")

    liste_a = [1, 4, 7]
    liste_b = [2, 3, 8, 9]
    print(fussion_liste(liste_a, liste_b))
    nombres = [3, 12, 7, 25, 8, 19, 2]
    print(caree_nombre_pair(nombres))
    
if __name__ == "__main__":
    main()