#Calculate sum of even numbers from 1 to 100
total=0
for i in range(1,101):
    if i%2==0:
        total+=i
print("Sum of even numbers is:",total)