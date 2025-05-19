from Final import book

def main():
    b = book()

    while True:
        v = input("Would you like to add a book? (  1.yes  /  2.no  /  3.show  /  4.delet  ) : ").strip().lower()

        if v == 'yes':
            b.Add() 
        
        elif v == 'no':
            print("Exiting.") 
            break
    
        elif v == 'show':
            b.showbook()

        elif v == 'delete':
            b.Minus()

        else:
            print("Invalid input. Please type (  1.yes  /  2.no  /  3.show  /  4.delet  ) : ")

if __name__ == '__main__':
    main()