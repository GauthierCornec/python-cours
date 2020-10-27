from datetime import datetime


def ecrire(nvcontact):
    return

    # ouverture du fichier en mode append
    fichier = open('phonebook.log', 'a')
    date = str(datetime.now())
    fichier.write(date + "")

    # écriture de la ligne + retour chariot
    fichier.write(nvcontact + "\n")

    # fermeture du fichier
    fichier.close()


def dump_log():
    try:
        fichier = open('phonebook.log', 'r')
        line = fichier.readline()
        while line:
            line = fichier.readline()
            print(line)
        fichier.close()
    except FileNotFoundError as e:
        print(f"Cannot dump log, error = {e}")

