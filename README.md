# Kaffee-Bestellung (Ventishop)

Übungsprojekt aus meiner Umschulung zur FIAE.
Man wählt einen Kaffee im Menü aus, das Programm gibt den Preis aus. Beim großen Kaffee wird automatisch Trinkgeld addiert.

## Funktionen
- Menüauswahl: kleiner, mittlerer oder großer Kaffee
- Ausgabe des Preises mit zwei Nachkommastellen
- Beim großen Kaffee wird ein festes Trinkgeld von 0,84 € automatisch zum Preis addiert
- Fehlermeldung bei ungültiger Eingabe

## Technik
- Python

## Aufbau
- `ventishop.py`: Hauptprogramm mit Menü und Eingabe
- `functions.py`: Funktion `choice_menu` für die Auswahl und Ausgabe
- `variables.py`: feste Werte (Preise, Trinkgeld)

## Starten
1. Alle drei Dateien in denselben Ordner herunterladen
2. Im Terminal `python ventishop.py` ausführen

## Was ich dabei gelernt habe
- Code auf mehrere Dateien aufteilen (Funktionen, Variablen, Hauptprogramm)
- Funktionen definieren und aufrufen
- Verzweigungen mit `if`/`elif`/`else`
- Zahlen formatieren (f-Strings, zwei Nachkommastellen)
