Name = []
DOB = []

with open ('DOB.txt', 'r+') as f:
    for line in f:
        space = line.split()
        name =space[:2]
        dob = space[2:]
        Name.append(" ".join(name))
        DOB.append(" ".join(dob))

print("NAME:\n", Name )
print("DOB:\n", DOB )






