masa = float(input("Podaj mase ciala w kg: "))
wzrost = float(input("Podaj wzrost w m: "))

BMI = masa/(wzrost)**2

print(round(BMI, 2))

if BMI < 18.5:
    print("Niedowaga")
elif BMI >= 18.5 and BMI < 25:
    print("Waga prawidlowa")
elif BMI >= 25 and BMI < 30:
    print("Nadwaga")
else:
    print("Otylosc")
