#To calculate Body Mass Index with certain criterias
#Inputs: Weight should be of int type, height should be of float
#Output: BMI should be a whole number

weight=int(input("Enter your weight in kilograms:"))
height=float(input("Enter your height in meters: "))
bmi= weight//(height**2)
print("Your Body Mass Index value is:",int(bmi))
