#To find the highest common factor of two numbers

def find_hcf(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find and display the HCF
hcf = find_hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is {hcf}.")
