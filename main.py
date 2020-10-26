def create_contact(Name, Phone, Fav):
    contact = {
        "Name": Name,
        "Phone": Phone,
        "Fav": Fav,
    }
    return contact

a = create_contact("Pierre", "123456789", True)
print(a)

b = create_contact("Jean", "234567890", True)
print(b)

c = create_contact("Jacques", "987654321", False)
print(c)

d = create_contact("Paul", "87654321", False)
print(d)

annuaire = {}

def add_contact(c):
    number_contact = c["Phone"]
    annuaire[number_contact] = c

Phone = input("Entrez votre numéro")
print(Phone)
Name = input("Entrez votre Nom")
print(Name)


contact = create_contact(Name, Phone, False)
add_contact(contact)
print(annuaire)


def get_names(n):
    names = []
    for k in annuaire:
        contact = annuaire[k]
        names.append(contact["Name"])
        names.sort()
        return names

def display_all():
    for Phone in annuaire:
        contact = annuaire[Phone]
        print(f'{Phone} => {contact}')

def get_contact(Phone):
    for k in annuaire:
        if k == Phone:
            return annuaire[k]