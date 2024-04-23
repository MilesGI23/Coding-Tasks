lunch = " I am going for lunch i fancy some chinese "
lch = ""

for _ in range(len(lunch)):
    if _ % 2 == 0:
        lch += lunch[_].upper()
    else:
        lch += lunch[_].lower()

print(lch)

lnglunch = lunch.split()

for _ in range(len(lnglunch)):
    if _ % 2 == 0:
        lnglunch[_] = lnglunch[_].upper()

print(" ".join(lnglunch))