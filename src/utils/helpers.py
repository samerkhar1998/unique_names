import difflib

def validInput(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard):
    if not isinstance(billFirstName, str) or not billFirstName.replace(" ", "").isalpha():
        raise ValueError("Invalid or missing 'bill first name': It must be a non-empty string.")
    if not isinstance(billLastName, str) or not billLastName.replace(" ", "").isalpha():
        raise ValueError("Invalid or missing 'bill last name': It must be a non-empty string.")
    if not isinstance(shipFirstName, str) or not shipFirstName.replace(" ", "").isalpha():
        raise ValueError("Invalid or missing 'ship first name': It must be a non-empty string.")
    if not isinstance(shipLastName, str) or not shipLastName.replace(" ", "").isalpha():
        raise ValueError("Invalid or missing 'ship last name': It must be a non-empty string.")
    if not isinstance(shipLastName, str) or not billNameOnCard.replace(" ", "").isalpha():
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

