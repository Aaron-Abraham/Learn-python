#Program to find maximum number from a list of numbers
num= list(map(int, input("Enter the list of numbers:\n").split()))
max_num=num[0]
for i in range(0,len(num)):
    if num[i]>max_num:
        max_num=num[i]

print("Maximum number:",max_num)