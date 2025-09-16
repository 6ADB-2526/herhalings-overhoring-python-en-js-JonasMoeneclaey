def checkIfPositive(getal1):
    while True:
        if getal1 >= 0:
            break
        else:
            getal1 = int(input("geef een positief getal op "))


x = int(input("geef een positief getal op. "))

checkIfPositive(x)