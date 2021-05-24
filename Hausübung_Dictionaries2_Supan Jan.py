#Try/except:
Woerterbuch_Deutsch ={"Apfel" : "apple",
              "Birne" : "pear",
              "Kirsche" : "cherry",
              "Melone" : "melon",
              "Marille" : "apricot",
              "Pfirsich" : "peach"
              }
                
Woerterbuch_Englisch = {"apple" : "Apfel",
              "pear" : "Birne",
              "cherry" : "Kirsche",
              "melon" : "Melone",
              "apricot" : "Marille",
              "peach" : "Pfirich"
              }

try:
    Eingabe = input("Welcher Begriff wird gesucht?: ") 
    print(Woerterbuch_Deutsch[Eingabe], "[EN]")
except KeyError: 
    try:
        print(Woerterbuch_Englisch[Eingabe], "[DE]")
    except KeyError:
        print("Wort wurde nicht gefunden!") 
