Eingabe=int(input("Anzahl der Iterationen:"))

sign = 1
pi_durch_4 = 0
for k in range(0,Eingabe) :
    pi_durch_4 += sign / (2*k+1)
    print(pi_durch_4, sign/(2*k+1), sign)
    sign = sign * (-1)
print("Das Ergebnis lautet:")
print(pi_durch_4*4)
