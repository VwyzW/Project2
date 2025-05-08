from Final import book

b = book()

v = ""

print(b.name)

while v != 'no':

    v = input("Would you like to add a book?'yes or no'(or 'find' to query)").strip().lower()
    if v == "yes":
        b.Add() 

    elif v == "no":
        print("Exiting.") 
        break
    
    elif v == "find":
        title = input("Enter the book title to find: \n").strip().upper()
        if title in b.book:
            info = b.book[title]
            print(f"\nFound '{title}':")
            print(" Author:", info['Author'])
            print(" Price: ",info['Price'])
    else:
        print("Invalid input. Please type 'yes' ,'find or no")
