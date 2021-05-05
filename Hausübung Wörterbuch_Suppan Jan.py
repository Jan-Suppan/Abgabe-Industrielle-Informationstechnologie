Woerterbuch_Deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich", "Bier"]
Woerterbuch_Englisch = ["apple", "pear", "cherry", "melon", "apricot", "peach", "beer"]

max = len(Woerterbuch_Deutsch)

eingabe = input("Zu übersetzender Begriff: ")

index = 0

while index < max:
    if Woerterbuch_Deutsch[index].lower() == eingabe.lower():
        print(Woerterbuch_Englisch[index], "[EN]")
        break
    if Woerterbuch_Englisch[index].lower() == eingabe.lower():
        print(Woerterbuch_Deutsch[index], "[DE]")
        break
    index +=1
    
if index == max:
    print("Eingabe nicht gefunden")
    print("Bis zum nächsten mal!")