# einfaches '=' Zeichen: Ist eine Zuweisung

strWetter = input("Wochenendwetter - 'sonnig' oder 'regnerisch'")

# doppeltes '==' Zeichen: Vergleichsoperator

if strWetter == "sonnig":
    print("Gartenparty")
    print("Yeah kaltes Bier in der Sonne!!!")
elif strWetter == "regnerisch":
    print("Kellerpartyparty")
    print("Yeah Bier!!!")
else: print("Bitte entweder 'sonnig' oder 'regnerisch' eingeben!")
