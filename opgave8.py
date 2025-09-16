getal1 = int(input("geef een getal op."))
getal2 = int(input("geef een nog getal op."))

kiesOperator = input("kies een operator tussen deze vier: +, -, *, /. ")

if kiesOperator == "+":
    print(getal1 + getal2)
elif kiesOperator == "-":
    print(getal1-getal2)
elif kiesOperator == "*":
    print(getal1*getal2)
elif kiesOperator == "/":
    print(getal1/getal2)