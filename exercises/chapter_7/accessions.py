import re

accs = "xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"
print("containing the number 5")
for acc in accs:
    if re.search(r"5", acc):
        print("\t" + acc)

print("containing d or e ")
for acc in accs:
    if re.search(r"(d|e)", acc):
        print("\t" + acc)

print("containing d followed by e ")
for acc in accs:
    if re.search(r"d.*e", acc):
        print("\t" + acc)

print("containing d followed by e with a single letter between them ")
for acc in accs:
    if re.search(r"d.e", acc):
        print("\t" + acc)

print("containing d and e in any order")
for acc in accs:
    if re.search(r"d.*e", acc) or re.search(r"e.*d", acc):
        print("\t" + acc)


print("starting with x or y")
for acc in accs:
    if re.search(r"^(x|y)", acc):
        print("\t" + acc)


print("starting with x or y and ending with e")
for acc in accs:
    if re.search(r"^(x|y).*e$", acc):
        print("\t" + acc)


print("three or more numbers in a row")
for acc in accs:
    if re.search(r"[0123456789]{3,100}", acc):
        print("\t" + acc)


print("three or more numbers in a row, more concisely")
for acc in accs:
    if re.search(r"\d{3,}", acc):
        print("\t" + acc)


print("ends with d and either a, r or p")
for acc in accs:
    if re.search(r"d[arp]$", acc):
        print("\t" + acc)

