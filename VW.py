from Final import book

b = book()


print(b.name)

v = input("Would you like to add a book?")
if v == "yes":    
    c = b.Add() 

elif v == "no":
    c = b.minus()