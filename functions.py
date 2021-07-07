# Multiple currency converter using functions
def converter(peso_type,dolar_value):
    if dolar_value == 0:
        print("You have $0.00 dolars")
    else:
        pesos = input("How many " + peso_type + " pesos do you have?: ")
        pesos = float(pesos)
        usd = pesos / dolar_value
        usd = round(usd,2)
        usd = str(usd)
        print("You have $" + usd + " dolars")

menu = """
Welcome to currency converter 💰💰💰

1 - Mexican Pesos
2 - Argentine Pesos
3 - Colombian Pesos

Select an option: """

option = int(input(menu))

if option == 1:
    converter("mexican", 19.95)
elif option == 2:
    converter("argentine", 95.94)
elif option == 3:
    converter("colombian", 3786.79)
else:
    print('Enter a valid option please')
    exit()