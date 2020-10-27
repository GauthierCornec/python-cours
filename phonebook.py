import logger



def create_contact(Name, Phones, Fav):
    try :
        contact = {
        "Name": Name,
        "Phone": Phones,
        "Fav": Fav,
        }
        return contact
    except IndexError as e:
        print(f"mon erreur = {e}")

annuaire = {}

def add_contact(new):
    logger.ecrire("ajout d'un contact")
    Phone = new["Phone"]
    annuaire[Phone] = new

def get_names(n):
    names = n["Name"]
    annuaire[get_names] = n
    return names

def get_numbers(c):
    phones = c["Phone"]
    annuaire[get_numbers] = c
    return phones

def get_fav(f):
    fav = f["Fav"]
    annuaire[get_fav] = f
    return fav

def get_contact(Phone):
    c = annuaire[Phone]
    logger.save_log(f"Getting contact={c}")
    return c

def disply_all():
    logger.dump_log()
    for a in annuaire:
        print(annuaire[a])







