import sys
import phonebook

args = sys.argv # récup les args
for i in range(0, len(args)): # boucle pour arg de 0 à la longueur des args.
    if args[i] == "-log":
        print("il est présent")

programme = True

while programme:
    names = input("Entrez nom du nouveau contact")
    phones = input("Entrez le nouveau numéro de tel")
    fav = input("est il favoris ?")

    c = phonebook.create_contact(names,phones, fav)
    phonebook.add_contact(c)
    print(phonebook.annuaire)