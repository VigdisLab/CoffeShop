#Definition einer Funktion
from variables import *

def choice_menu(eingabe):
    pass
    if eingabe == 1:
        print(f"Du hast dich für den kleinen Kaffee für einen Preis von {coffee_small_size:.2f} € entschieden.")
    elif eingabe == 2:
        print(f"Du hast dich für einen mittleren Kaffee für einen Preis von {coffee_medium_size:.2f} € entschieden." )
    elif eingabe == 3:
        summary = coffee_large_size + tip
        summary = str(f"{summary:.2f}").replace(".",",")
        print(f"Du hast dich für einen großen Kaffee für einen Preis von {summary} € entschieden.")
    else:
        print("Dieses Menü gibt es nicht, bitte wiederhole den Bestellvorgang.")
