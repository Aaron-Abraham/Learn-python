#Pizza ordering menu

size= int(input("Select your pizza size of choice:\n1.Small pizza\n2.Medium pizza\n3.Large pizza\n"))
bill=0
if size==1:
    print("Price for small pizza is Rs 100.")
    bill+=100
elif size==2:
    print("Price for medium pizza is Rs 200.:")
    bill+=200
elif size==3:
    print("Price for large pizza is Rs 300")
    bill+=300
else:
    print("Choose an option from the listed.")

#Ask for toppings
add_pepperoni=input("Would you like to add pepperoni to the pizza?(Y/N)")
if add_pepperoni.lower()=='y':
    if size==1:
        bill+=30
    else:
        bill+=50

add_cheese=input("Add extra cheese? (Y/N)")
if add_cheese.lower()=='y':
    bill+=20

print("Your total bill amount:",bill)
