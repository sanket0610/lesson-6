
w=int(input("Enter your weight in KG"))
h=float(input("Enter your height in metres"))

bmi=w/(h**2)

if bmi<18:
    print("You are under weight")
elif bmi>=18 and bmi<25:
    print("You are healthy")
else:
    print("You are over weight")