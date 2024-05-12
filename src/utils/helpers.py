import difflib

def validInput(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard):
    if not billFirstName or not isinstance(billFirstName, str):
        raise ValueError("Invalid or missing 'bill first name': It must be a non-empty string.")
    if not billLastName or not isinstance(billLastName, str):
        raise ValueError("Invalid or missing 'bill last name': It must be a non-empty string.")
    if not shipFirstName or not isinstance(shipFirstName, str):
        raise ValueError("Invalid or missing 'ship first name': It must be a non-empty string.")
    if not shipLastName or not isinstance(shipLastName, str):
        raise ValueError("Invalid or missing 'ship last name': It must be a non-empty string.")
    if not billNameOnCard or not isinstance(billNameOnCard, str):
        raise ValueError("Invalid or missing 'bill card': It must be a non-empty string.")

def normalize(firstName, lastName):
    name = firstName.lower().split()
    middleName = None
    if len(name) > 1:
        middleName = name[-1]
    name = name[0]
    return name, middleName, lastName.lower()
def correctTypos(name, allNames):
    closestName = difflib.get_close_matches(name, allNames, n=1, cutoff=0.75)
    if closestName:
        return closestName[0]
    return name

def isNickName(name, nicknames):
    return True if name in nicknames else False

def isSamePerson(firstPerson, secondPerson):
    # First name checks
    if firstPerson.firstName != secondPerson.firstName:
        return False

    # Middle name checks
    elif secondPerson.middleName and firstPerson.middleName and secondPerson.middleName != firstPerson.middleName:
        return False

    # Last name checks
    elif firstPerson.lastName != secondPerson.lastName:
        return False

    return True