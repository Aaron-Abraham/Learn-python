#To calculate how much days, weeks, months we have left till we turn 90 yrs old
age= int(input("Enter your current age:"))

year_left= 90-age
days_left= year_left*365
weeks_left= year_left*52
months_left= year_left*12

print(f"You have {days_left} days,{weeks_left} weeks and {months_left} months till you turn 90.")