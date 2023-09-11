#Introduction
print("Welcome to your one and only Egyptian Pounds currency converter ᕕ(︶‿︶)ᕗ \n")

#please type the amount
amount = float(input("Please type how much Egyptian Pounds you want to convert: \n"))
if amount < 0 :
    print("\nYou're in debt (╥_╥)"), exit()

if amount == 0 :
    print("\nYou're broke (╥_╥)"), exit()

#please choose the currency
cur = input("\nPlease choose the currency you want to convert to (Dollar/Euro/Pound Sterling):\n").lower()

#result
if cur == "dollar":
    print("\nThat will be:", amount / 30.90, "USD ")
elif cur == "euro":
    print("\nThat will be:", amount / 33.64, "Euros")
elif cur == "pound sterling":
    print("\nThat will be:", amount / 39.33, "Pound Sterling")
else:
    print("\nPlease choose from (Dollar/Euro/Pound Sterling) and try again")