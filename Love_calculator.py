#Game: Love Calculator

name= str(input("Enter your his name:"))
name2= str(input("Enter you her name:"))

combine= name+name2
low_case=combine.lower()

t=low_case.count('t')
r=low_case.count('r')
u=low_case.count('u')
e=low_case.count('e')
true=t+r+u+e

l=low_case.count('l')
o=low_case.count('o')
v=low_case.count('v')
e=low_case.count('e')
love=l+o+v+e 

love_score= int(str(true)+str(love))
if love_score<10 or love_score>90:
    print(f"Your love score is {love_score}% and you go together.")
elif love_score>=40 and love_score<=50 :
    print(f"Your love score is {love_score}% and it's a match made in heaven!")
else:
    print(f"Your love score is {love_score}%.")