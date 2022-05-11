import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calculator():
    choice = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    number1 = float(input("Podaj składnik 1.:"))
    number2 = float(input("Podaj składnik 2.:"))
    if choice == 1:
        logging.info(f"Dodaję {number1} i {number2}")
        result = number1 + number2
    elif choice == 2:
        logging.info(f"Odejmuję {number2} od {number1}")
        result = number1 - number2
    elif choice == 3:
        logging.info(f"Mnożę {number1} przez {number2}")
        result = number1 * number2
    elif choice == 4:
        logging.info(f"Dzielę {number1} przez {number2}")
        result = number1 / number2
    else:
        result = 0
    return print(f"Wynik to {result}")

calculator()