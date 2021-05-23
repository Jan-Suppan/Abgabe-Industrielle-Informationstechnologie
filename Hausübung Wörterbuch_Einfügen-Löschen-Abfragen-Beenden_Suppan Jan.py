Woerterbuch_Deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich", "Bier"]
Woerterbuch_Englisch = ["apple", "pear", "cherry", "melon", "apricot", "peach", "beer"]

max = len(Woerterbuch_Deutsch)

running = True
while running:
    print("Welchen Befehl möchten Sie durchführen?")
    auswahl = input("[E]infügen, [L]öschen, [A]bfragen, [B]eenden: ")

# Einfügen
    if auswahl == 'E' or auswahl == 'e':
        Wort_DE = input("Welches deutsche Wort möchten Sie hinzufügen: ")
        Woerterbuch_Deutsch.append(Wort_DE)
        Wort_EN = input("Geben Sie nun das englische Wort dazu ein: ")
        Woerterbuch_Englisch.append(Wort_EN)
        print("Das aktualisierte Wörterbuch lautet: ")
        print(Woerterbuch_Deutsch)
        print(Woerterbuch_Englisch)
        continue

# Löschen
    elif auswahl == 'L' or auswahl == 'l':
        print("Diese Wörter stehen zum Löschen zur Auswahl: ")
        print(Woerterbuch_Deutsch)
        print(Woerterbuch_Englisch)
        
        Wort = input("Welches Wort möchten Sie löschen: ")
        
        Index_Wort = 0
        k = 0
        Iterationen = len(Woerterbuch_Deutsch)
        
        while k < Iterationen:
            
            if Woerterbuch_Deutsch[k].lower() == Wort.lower():
                Index_Wort = k
                Woerterbuch_Deutsch.remove(Woerterbuch_Deutsch[Index_Wort])
                Woerterbuch_Englisch.remove(Woerterbuch_Englisch[Index_Wort])
                print("Das aktualisierte Wörterbuch lautet: ")
                print(Woerterbuch_Deutsch)
                print(Woerterbuch_Englisch)
                break
                
            elif Woerterbuch_Englisch[k].lower() == Wort.lower():
                Index_Wort = k
                Woerterbuch_Deutsch.remove(Woerterbuch_Deutsch[Index_Wort])
                Woerterbuch_Englisch.remove(Woerterbuch_Englisch[Index_Wort])
                print("Das aktualisierte Wörterbuch lautet: ")
                print(Woerterbuch_Deutsch)
                print(Woerterbuch_Englisch)
                break  
            k +=1
            
        if k == len(Woerterbuch_Deutsch):
            print("Eingabe nicht gefunden!") 
        continue

# Abfragen
    elif auswahl == 'A' or auswahl == 'a':
        eingabe = input("Zu übersetzender Begriff: ")
        
        index = 0
        i = 0
        Iterationen_2 = len(Woerterbuch_Deutsch)
       
        while i < Iterationen_2:
            if Woerterbuch_Deutsch[i].lower() == eingabe.lower():
                index = i
                print(Woerterbuch_Englisch[index], "[EN]")
                break
                
            if Woerterbuch_Englisch[i].lower() == eingabe.lower():
                index = i
                print(Woerterbuch_Deutsch[index], "[DE]")
                break
            i += 1
            
        if  i == len(Woerterbuch_Deutsch):
            print("Eingabe nicht gefunden!")

# Beenden
    else: 
        print("Tschüss!")
        exit()
        



           