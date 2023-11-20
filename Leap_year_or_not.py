#Check whether a year is leap year or not
year=int(input("Enter year:"))
"""
if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
    print("Leap year")
else:
    print("Not Leap Year")
"""
if(year%4==0):
    if(year%100==0):
        if(year%4==0):
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
    