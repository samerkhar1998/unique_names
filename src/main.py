import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils.helpers import validInput, correctTypos, normalize, isNickName
from src.classes.person import Person
from src.utils.parse_names_csv import parse_names_csv

def countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard):
    print("bill first-name: {}, bill last-name: {}, ship first-name: {}, ship last-name: {}, bill name on card: {}".format(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard))

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = os.path.join(ROOT_DIR, '../data/name_to_nick.csv')

    nicknameToName, nameToNickname = parse_names_csv(CONFIG_PATH)
    try:
        validInput(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard)
    except ValueError as e:
        print(e)
        return 0


    # Normalize all the names to be in a lower case
    billNameOnCard = set(billNameOnCard.lower().split())
    normBillFirst, normBillMiddle, normBillLast = normalize(billFirstName, billLastName)
    normShipFirst, normShipMiddle, normShipLast = normalize(shipFirstName, shipLastName)

    # Correct misspellings of first name
    normBillFirst = correctTypos(normBillFirst, nameToNickname.items())
    normShipFirst = correctTypos(normShipFirst, nameToNickname.items())

    # Correct misspellings of last name
    normBillLast = correctTypos(normBillLast, billNameOnCard)
    normShipLast = correctTypos(normShipLast, billNameOnCard)

    bill = Person(normBillFirst, normBillMiddle, normBillLast)
    ship = Person(normShipFirst, normShipMiddle, normShipLast)

    if isNickName(bill.firstName, nicknameToName.keys()):
        bill.possibleNames = nicknameToName[bill.firstName]
        bill.possibleNicknames.add(bill.firstName)
    else:
        bill.possibleNames.add(bill.firstName)
        bill.possibleNicknames.update(nameToNickname[bill.firstName])

    if isNickName(ship.firstName, nicknameToName.keys()):
        ship.possibleNames = nicknameToName[ship.firstName]
        ship.possibleNicknames.add(ship.firstName)
    else:
        ship.possibleNames.add(ship.firstName)
        ship.possibleNicknames.update(nameToNickname[ship.firstName])

    if bill == ship:
        return 1

    return 2

if __name__ == '__main__':
    print('unique_names main started')
    print("unique_names: " + str(countUniqueNames("Deborah", "Egli", "debbie", "egli", "Deborah Egli")))
    print("unique_names: " + str(countUniqueNames("Deborah", "Egni", "debbie", "egli", "Deborah Egli")))