import csv
from collections import defaultdict
def parse_names_csv(file_path):
    nicknameToName = defaultdict(set)
    nameToNickname = defaultdict(set)
    with open(file_path) as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            primaryName = row[0].lower()
            nameToNickname[primaryName] = set()
            for nn in row[1:]:
                nickname = nn.lower()
                # if not nicknameToName[nickname]:
                #     nicknameToName[nickname] = set()
                nicknameToName[nickname].add(primaryName)
                nameToNickname[primaryName].add(nickname)

    return nicknameToName, nameToNickname
