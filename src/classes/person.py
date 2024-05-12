from src.utils.helpers import correctTypos, normalize, isNickName
class Person:
    def __init__(self, firstName, lastName, nameToNickname, nicknameToName, billNameOnCard):

        normFirstName, normMiddleName, normLastName = normalize(firstName, lastName)
        normFirstName = correctTypos(normFirstName, nameToNickname.items())
        normLastName = correctTypos(normLastName, billNameOnCard)

        self.possibleNames = set()
        self.firstName = normFirstName
        self.possibleNicknames = set()
        self.middleName = normMiddleName
        self.lastName = normLastName

        if isNickName(self.firstName, nicknameToName.keys()):
            self.possibleNames = nicknameToName[self.firstName]
            self.possibleNicknames.add(self.firstName)
        else:
            self.possibleNames.add(self.firstName)
            self.possibleNicknames.update(nameToNickname[self.firstName])

    def __eq__(self, other):
        if not isinstance(other, Person):
            # don't attempt to compare against unrelated types
            return NotImplemented

        if not self.possibleNames.intersection(other.possibleNames):
            return False

        if not self.lastName == other.lastName:
            return False

        if self.middleName and other.middleName and not self.middleName == other.middleName:
            return False

        return True
