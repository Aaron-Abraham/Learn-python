#Who pay's the bill

import random

names=input("Enter the names who decides to pay the bill:\n")
names_split=names.split(",")
names_len=len(names_split)
num=random.randint(0,names_len-1)
print(f"The lucky person to pay is {names_split[num]}")
