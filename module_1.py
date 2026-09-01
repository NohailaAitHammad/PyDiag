nom  =  "Karim"
prenom  =  "Ben  Ali"
notes  =  [12,  15,  9]

somme = 0

for note in notes:
    somme += note
print(f"{nom} moyenne : {somme / 3:>6.2f}")

#Défis supplémentaires


notesInput = []
nomInput = input("Veuillez saisir votre nom: ")
prenomInput = input("Veuillez saisir votre prenom: ")


while len(notesInput) < 3:
    noteInput = input(f"Veuillez saisir  note: ")
    if not noteInput.isdigit():
        print("Ce  n’est  pas  un  nombre  valide,  reessayez.")
    else:
        print(f"Note  acceptee : {float(noteInput)}")
        notesInput.append(float(noteInput))

