# Currency Converter from MXN
pesos = input("How many pesos do you have?: ")
pesos = float(pesos)

dolar_value = 20

usd = pesos / dolar_value
usd = round(usd,2)

usd = str(usd)
print("You have $" + usd + " dolars")
