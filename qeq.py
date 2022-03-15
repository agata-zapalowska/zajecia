import cmath

a = float(input("Podaj wspolczynnik a nalezacy do liczb rzeczywistych: "))
b = float(input("Podaj wspolczynnik b nalezacy do liczb rzeczywistych: "))
c = float(input("Podaj wspolczynnik c nalezacy do liczb rzeczywistych: "))

delta = b**2-4*a*c
pierwiastek = cmath.sqrt(delta)

if a==0:
    print("Nie jest to funkcja kwadratowa")
elif delta==0:
    print("Miejsce zerowe: ",  -b/(2*a))
elif delta!=0:
    print("Miejsca zerowe: ", (-b+pierwiastek)/(2*a), (-b-pierwiastek)/(2*a))
