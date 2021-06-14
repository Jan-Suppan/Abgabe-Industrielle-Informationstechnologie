woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich", "Bier"]
woerterbuch_englisch = ["apple", "pear", "cherry", "melon", "apricot", "peach", "beer"]
 
def sucheWord(wordInput):                          
    index = 0
    for wort in woerterbuch_deutsch:    # Wenn Wort im Wörterbuch vorhanden -> Ausgabe Index
        if wordInput.lower() == wort.lower():  
            break
        index +=1   
    
    if index == len(woerterbuch_deutsch):
        index=0
        for wort in woerterbuch_englisch:          
            if wordInput.lower() == wort.lower():
                break
            index +=1    
        
        if index == len(woerterbuch_englisch):
            raise Exception("Das Wort steht nicht im Wörterbuch")    # Sonst -> Ausgabe "Das Wort steht nicht im Wörterbuch"  
    return (woerterbuch_deutsch[index], woerterbuch_englisch[index], index)

def einfügenWord(deutschesWort, englischesWort):   # Einfügen
    try:
        sucheWord(deutschesWort)                   # Funktion ob Wort im Wörterbuch nicht schon vorhanden ist.
        print("Wort bereits im Wörterbuch")        # Wenn vorhanden -> Ausgabe "Wort bereits im Wörterbuch" 
    except:
        Stelle = input("Nach der wie vielten Stelle soll das Wort im Wörterbuch eingefügt werden?: ")   
        intStelle = int(Stelle)                                 # Eingebenen Wert in Integer umwandeln
        woerterbuch_deutsch.insert(intStelle, deutschesWort)    # .insert zum hinzufügen von Wörter an einer Liste
        woerterbuch_englisch.insert(intStelle, englischesWort)

def loeschenWord():
    try:
        output = sucheWord(input("Welches Wort wollen Sie löschen?: "))   # Löschen
        woerterbuch_deutsch.remove(output[0])                            
        woerterbuch_englisch.remove(output[1])
    except Exception as e:                                                # Wenn try nicht funktioniert, akzeptiere die Fehlermeldung und gib sie aus.
        print(e)
        
def uebersetzenWord():
    try:
        output = sucheWord(input("Zu übersetzendes Wort: "))              # Übersetzen
        print(output[0] + "[DE]")                                        
        print(output[1]+ "[EN]")                                        
    except Exception as e:                                                # Wenn try nicht funktioniert, akzeptiere die Fehlermeldung und gib sie aus.
        print(e)
              
def eingabeBefehl():                                                      
    while True:                                     
        auswahl = input("Befehl? \n[E]infügen \n[L]öschen \n[A]bfrage \n[B]eenden: ")
        if auswahl.lower() == "e" or  auswahl.lower() =="l" or auswahl.lower() =="a" or auswahl.lower() =="b":   # wenn die Eingabe des Buchstaben mit einem angegebenen Buchstaben übereinstimmt,
            return auswahl.lower()                                                                               # gib diesen Buchstaben weiter
        else:
            print("Falsche Eingabe!")                                                                            #ansonst "Falsche Eingabe"
    
while True:
    auswahl = eingabeBefehl()                             
    if auswahl == "e":
        einfügenWord(input("Bitte geben Sie das einzufügende Wort zuerst auf Deutsch ein: "), input("Bitte geben Sie das zugehörende englische Wort ein: "))
        
    elif auswahl == "l":
        loeschenWord()
    elif auswahl == "b":
        print("Tschüss!")
        break   
    else:
        uebersetzenWord()
        
    print("Das aktuelle Wörterbuch lautet:")
    print(woerterbuch_deutsch)
    print(woerterbuch_englisch)