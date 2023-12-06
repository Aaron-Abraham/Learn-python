#Program to calculate average height from a list of heights

height=list(map(int,input("Enter your heights:").split()))
count=0
total=0
for i in height:
    count+=1
for i in height:
    total+=i
avg=total/count
print("Average height is:",avg)
