# Multiple currency converter using conditional statements
menu = """
Welcome to currency converter 💰💰💰

1 - Mexican Pesos
2 - Argentine Pesos
3 - Colombian Pesos

Select an option: """
option = int(input(menu))

if option == 1:
    dolar_value = 19.95
elif option == 2:
    dolar_value = 95.94
elif option == 3:
    dolar_value = 3786.79
else:
    print('Enter a valid option please')
    exit()


# Currency Converter
pesos = input("How many pesos do you have?: ")
pesos = float(pesos)


usd = pesos / dolar_value
usd = round(usd,2)

usd = str(usd)
print("You have $" + usd + " dolars")
