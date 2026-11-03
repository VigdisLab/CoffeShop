from variables import *
from functions import choice_menu


eingabe = int(input(f"""
HERZLICH WILLKOMMEN in unserem Cafe
    
        Bitte wähle aus den folgenden Menüs:
        1: Kleiner Kaffee für {coffee_small_size} €
        2: Mittlerer Kaffee für {coffee_medium_size} €
        3: Großer Kaffee für {coffee_large_size} €
"""))

#Aufruf einer Funktion
#Erst kommt die Definition und danach erfolgt der Aufruf!
choice_menu(eingabe)


# """ Kommentare: """

# Datentypen
# string = "Das ist ein Satz in Form von einem String"
# int = 10
# float = 1.75

#BuildIn Functions
#print()
#input()
#int()
#replace()