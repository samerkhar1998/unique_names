class Person:
    def __init__(self, firstName, middleName, lastName):
        self.possibleNames = set()
        self.firstName = firstName
        self.possibleNicknames = set()
        self.middleName = middleName
        self.lastName = lastName

    def __eq__(self, other):
        if not isinstance(other, Person):
            # don't attempt to compare against unrelated types
            return NotImplemented

        if not self.possibleNames.intersection(other.possibleNames):
            return False
        if not self.possibleNicknames.intersection(other.possibleNicknames):
            return False

        if not self.lastName == other.lastName:
            return False

        if self.middleName and other.middleName and not self.middleName == other.middleName:
            return False

        return True
