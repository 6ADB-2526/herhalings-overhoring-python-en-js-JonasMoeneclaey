teRadenGetal = int(input("geef een getal op die de andere persoon moet raden. "))

raadHetGetal = int(input("geef een getal op "))
while True:
    if teRadenGetal == raadHetGetal:
        break
    else:
        raadHetGetal = int(input("geef een getal op "))