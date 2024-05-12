import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils.helpers import validInput
from src.classes.person import Person
from src.utils.parse_names_csv import parse_names_csv

def countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard):
    print("Bill Full Name: {} {} | Ship Full Name: {} {} | bill name on card: {}".format(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard))

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = os.path.join(ROOT_DIR, '../data/name_to_nick.csv')

    nicknameToName, nameToNickname = parse_names_csv(CONFIG_PATH)
    try:
        validInput(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard)
    except ValueError as e:
        print(e)
        return -1

    # Normalize all the names to be in a lower case
    billNameOnCard = set(billNameOnCard.lower().split())
    # constructor of person handles typos
    bill = Person(billFirstName, billLastName, nameToNickname, nicknameToName, billNameOnCard)
    ship = Person(shipFirstName,shipLastName, nameToNickname, nicknameToName, billNameOnCard)

    if bill == ship:
        return 1

    return 2

if __name__ == '__main__':
    print('unique_names examples:')
    print("unique names: " + str(countUniqueNames("Deborah", "Egli", "Deborah", "Egli", "Deborah Egli")))
    print("unique names: " + str(countUniqueNames("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli")))
    print("unique names: " + str(countUniqueNames("Deborah", "Egni", "Deborah", "Egli", "Deborah Egli")))
    print("unique names: " + str(countUniqueNames("Deborah S", "Egli", "Deborah", "Egli", "Deborah Egli")))
    print("unique names: " + str(countUniqueNames("Michele", "Egli", "Deborah", "Egli", "Michele Egli")))
