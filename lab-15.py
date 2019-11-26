baseballTeam = { "Jodi", "Carmen", "Aida", "Alicia"}
basketballTeam = { "Eva", "Carmen", "Alicia", "Sarah"}

def printLine():
    print("\n")

print("Members of the baseball team:")
for member in baseballTeam:
    print(member)

printLine()

print("Members of the basketball team:")
for member in basketballTeam:
    print(member)

printLine()

print("Members that play both baseball and basketball:")
for member in baseballTeam.intersection(basketballTeam):
    print(member)

printLine()

print("Members that play either baseball or basketball:")
for member in baseballTeam.union(basketballTeam):
    print(member)

printLine()

print("Members that play baseball, but not basketball:")
for member in baseballTeam.difference(basketballTeam):
    print(member)

printLine()

print("Members that play basketball, but not baseball:")
for member in basketballTeam.difference(baseballTeam):
    print(member)

printLine()

print("Members that play one sport, but not both:")
for member in (baseballTeam.union(basketballTeam)).difference(baseballTeam.intersection(basketballTeam)):
    print(member)