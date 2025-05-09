from Final import book

b = book()

v = ""

print(b.name)

while True:

    v = input("Would you like to add a book?'yes or no (show or delete)'").strip().lower()
    if v == "yes":
        b.Add() 

    elif v == "no":
        print("Exiting.") 
        break
    
    elif v == "show":
        b.showbook()

    elif v == 'delete':
        b.Minus()

    else:
        print("Invalid input. Please type 'yes or no (show or delete)'")
  