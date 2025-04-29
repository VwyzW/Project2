from Final import book

b = book()

v = ""

print(b.name)

while v != 'no':

    v = input("Would you like to add a book?'yes or no'")
    if v == "yes":
        c = b.Add() 

    elif v == "no":
        c = b.minus()