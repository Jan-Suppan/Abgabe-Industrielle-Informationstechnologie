# Aufgabe 1:
# Schreiben Sie ein Python-Programm, das
# 1) den Benutzer begrüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahlentgegen nimmt
# 4) die Summe der beiden Zahlen berechnet und ausgibt
# 5) die Differenz der kleineren von der größeren Zahlen berechnet und ausgibt
# 6) das Produkt der beiden Zahlen berechnet und ausgibt
# 7) den Quotient der kleineren Zahl durch die größere Zahl berechnet und ausgibt (inkl. Nachkommastellen)

print("Hallo, BenutzerIn!")

Zahl_1 = float(input("Eingabe der 1. Zahl: "))
Zahl_2 = float(input("Eingabe der 2. Zahl: "))

#Summe
print("Summe:" , Zahl_1+Zahl_2)

#Differenz
if Zahl_2 < Zahl_1:
    Differenz = Zahl_2 - Zahl_1
    
elif Zahl_1 < Zahl_2:
    Differenz = Zahl_1 - Zahl_2
    
elif Zahl_1 == Zahl_2:
    Differenz = Zahl_1 - Zahl_2
   
print("Differenz:" , Differenz)

#Produkt
print("Produkt:" , Zahl_1*Zahl_2)

#Divison
if Zahl_2 < Zahl_1:
    Quotient = Zahl_2 / Zahl_1
    
elif Zahl_1 < Zahl_2:
    Quotient = Zahl_1 / Zahl_2
    
elif Zahl_1 == Zahl_2:
    Quotient = Zahl_1 / Zahl_2
   
print("Quotient:" , Quotient)




