
class BMI():

    def bmic(**kwargs):
        wei = kwargs['wei']
        hei = kwargs['hei']

        return wei / (hei)**2

    def choose(**bmi):
        chosen = bmi['chosen']
        change = {
        chosen<18.5:"You are underweight",
        18.5<=chosen<25:"You are normal weight",
        25<=chosen<30:"YOu are Overweight",
        30<=chosen<35:"You are Obsesity class I",
        35<=chosen<40:"You are Obsesity class II",
        chosen>=40:"You are Obsesity class III"
        }
        ans = change.get(True,"A trouble appear")
        return ans
        

bmi = BMI

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

heit = height / 100
j =bmi.bmic(wei = weight, hei = heit)
print("The BMI is", j)
print(bmi.choose(chosen = j))

