inches_to_cm = 2.54

while True:
    inches = float(input("Enter a value in inches, if you want to exit enter a negative value: "))
    if inches < 0:
        print("Negative value entered. Program terminated.")
        break
    centimeters = inches * inches_to_cm
    print(f"{inches} inches is equal to {centimeters} centimeters.")


