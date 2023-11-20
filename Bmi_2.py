#Calculate bmi and classify them to categories like: underweight, normal, overweight, obese

weight = float(input("Enter your weight in kgs:"))
height = float(input("Enter your height in meters:"))
bmi= weight/height**2

if bmi<16.0:
    print("You are underweight")
elif bmi>=16.0 and bmi<=18.4:
    print("You are underweight and moderately thin")
elif bmi>18.4 and bmi<25.0:
    print("You are in normal range.")
elif bmi>25.0 and bmi<29.9:
    print("You are overweight.")
else:
    print("You are obese.")

