from Final import book

def main():
    b = book()

    while True:
        v = input("Would you like to add a book?'yes or no (show or delete(remove))'").strip().lower()
        if v == 'yes':
            b.Add() 
        
        elif v == 'no':
            print("Exiting.") 
            break
    
        elif v == 'show':
            b.showbook()

        elif v == 'delete' or 'remove':
            b.Minus()

        else:
            print("Invalid input. Please type 'yes or no (show or delete(remove))'")

if __name__ == '__main__':
    main()