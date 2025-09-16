getal1 = int(input("geef een getal op."))
getal2 = int(input("geef een nog getal op."))

kiesOperator = input("kies een operator tussen deze vier: +, -, *, /. ")

optellen = "+"
aftrekken = "-"
vermenigvuldigen = "*"
delen = "/"

if kiesOperator == optellen:
    print(getal1 + getal2)
elif kiesOperator == aftrekken:
    print(getal1-getal2)
elif kiesOperator == vermenigvuldigen:
    print(getal1*getal2)
elif kiesOperator == delen:
    print(getal1/getal2)