# Schleifenvariable oder auch Zählvariable: i, j, k

counter1 = 10
while counter1 >= 0:
    counter1 = counter1-1 # oder counter -=1
    print(counter1)
    
# Addieren Sie in einer Schleifen die Zahlen von 1 bis 100 und geben Sie das Ergebnis aus

n = 100
counter2 = 0
i = 1
while i <= n:
    counter2 = counter2 + i
    i = i + 1

print("Die Summe lautet: ", counter2)


