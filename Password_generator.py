#Python project-2
#Password generator
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')']
print("Welcome to Password Generator!")
n_letters=int(input("How many letters you want in your password:\n"))
n_symbols=int(input("How many symbols do you require:\n"))
n_numbers=int(input("How many numbers do you require:\n"))
password=[]

for i in range(1,n_letters+1):
    temp_ch=random.choice(letters)
    password.append(temp_ch)

for i in range(1,n_symbols+1):
    temp_ch=random.choice(symbols)
    password.append(temp_ch)

for i in range(1,n_numbers+1):
    temp_ch=random.choice(numbers)
    password.append(temp_ch)

random.shuffle(password)
pswd=''
for i in password:
    pswd+=i
print(pswd)
