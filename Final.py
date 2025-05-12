import os
import json

class book():
    DATA_FILE = 'books.TJay'

    def __init__(self):
        if os.path.exists(self.DATA_FILE):
            try:
                with open(self.DATA_FILE, 'r', encoding='utf-8') as f:
                    self.Books = json.load(f)
            except:
                self.Books = {}
        else:
            self.Books = {}

    def save(self):
        with open(self.DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.Books, f, ensure_ascii=False, indent=2)
        

    def Add(self):
        title = input("Enter the name of the book you add: \n").strip().upper()
        author = input("Enter the author of the book you add: \n").strip()
        try:
            price = float(input("Enter the listing price the book: \n"))
        except ValueError:
            print("The price format is incorrect, failed to add。")
            return
        
        self.Books[title] = {'Author': author,'Price': price}
        print(f"you have added {title}\n")
        print(self.Books)

    def muins(self):
        title = input("enter the name of the bookyou remove: \n").strip().upper()
        if title in self.Books:
            del self.Books[title]
            print(f"Remove {title}.\n")
        else:
            print(f"Book not found: {title}\n")


    def showbook(self):
        if not self.Books:
            print("No books in library.")
            return
        for x in self.Books.items():
            print(x)
            print(self.Books[x]["auther"])
            print(self.Books[x]["price"])

        print()
   