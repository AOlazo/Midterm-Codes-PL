
def bmi_cal(**kwargs):
    weight = kwargs['weight']
    height = kwargs['height']

    return weight/(height)**2

hei = float(input("Enter height in cm: "))
wei = float(input("Enter your weight in kg: "))

heit = hei / 100
bmi = bmi_cal(weight = wei, height = heit)

print("Your BMI is ", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi == 18.5 or bmi <= 24.9:
    print("Normal Weight")
elif bmi == 25.0 or bmi <= 29.9:
    print("Overweight")
elif bmi == 30.0 or bmi <= 34.9:
    print("Obsesity Class I")
elif bmi == 35.5 or bmi <= 39.9:
    print("Obsesity Class II")
elif bmi >= 40.0:
    print("Obsesity Class III")
else:
    print("Invalid Input")



