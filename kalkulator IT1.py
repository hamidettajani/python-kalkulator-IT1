print("1.Addisjon (+) :")
print("2.Subtraksjon (-) :")
print("3.Multiplikasjon (*) :")
print("4.Divisjon (/) :")
    
def addisjon(x,y):
    return x + y
def subtraksjon(x,y):
    return x - y
def multiplikasjon(x,y):
    return x * y
def divisjon(x,y):
    return x / y
def addisjon3(x,y,z):
    return x + y + z

regnestykke = input("Velg ønsket operatør: ")
if regnestykke in ('1','2','3','4','5'):
    tall1 = int(input("Skriv inn ditt første tall :"))
    tall2 = int(input("Skriv inn ditt andre tall :"))
    tall3 = int(input("Skriv inn ditt tredje tall :"))

    if regnestykke == '1':
        print(tall1, "+", tall2, "=", addisjon(tall1,tall2))
    elif regnestykke == '2':
        print(tall1, "-", tall2, "=", subtraksjon(tall1,tall2))
    elif regnestykke == '3':
        print(tall1, "*", tall2, "=", multiplikasjon(tall1,tall2))
    elif regnestykke == '4':
        print(tall1, "/", tall2, "=", divisjon(tall1,tall2))
    elif regnestykke == '5':
        print(tall1, "+", tall2, "+", tall3, "=", addisjon3(tall1,tall2,tall3))
        