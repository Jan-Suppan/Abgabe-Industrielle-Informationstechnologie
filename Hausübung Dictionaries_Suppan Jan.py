# Dictionaries
woerterbuch = {"Apfel": "apple",
               "Birne": "pear"}
try:
    print(woerterbuch[input("Begriff: ")]) # Nur KeyError
except:
    print("Das Wort existiert nicht")

while True: # Eingabe solange bis eine Zahl eingegeben wurde!
    try:
        stringA = input("Zahl: ")
        intb= int(stringA) # Umwanldung String to Int => nur ValueError möglich
        break
    except ValueError:
        print("Kein gültiger Wert -> bitte Neueingabe")
print("fertig")