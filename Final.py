class book():
    def __init__(self):
        self.index_file = 'index.txt'
        
        try:
            with open(self.index_file, 'r', encoding='utf-8') as f:
                self.title = [line.strip().upper() for line in f if line.strip()]
        except FileNotFoundError:
            with open (self.index_file, 'w', encoding='utf-8'):
                pass
            self.books = []

    def save(self):
        with open(self.index_file, 'w',encoding='utf-8') as f:
            for t in self.books:
                f.write(t + '\n')

    def Add(self):
        self.title = input("Enter the name of the book you add: \n").strip().upper()
        if self.title in self.books:
            print(f"Book '{self.title}' already exists.\n")
            return
        self.author = input("Enter the author of the book you add: \n").strip()
        try:
            self.price = float(input("Enter the listing price the book: \n"))
        except ValueError:
            print("The price format is incorrect, failed to add.")
            return
        fname = f"{self.title}.txt"
        with open(fname ,'w' ,encoding='utf-8') as f:
            f.write(f"author: {self.author}\n")
            f.write(f"price: {self.price}\n")
        self.books.append(self.title)
        self.save
        print(f"You have added. '{self.title}'.\n")

    def Minus(self):
        self.title = input("Enter the name of the bookyou remove: \n").strip().upper()
        if self.title not in self.books:
            print(f"Book not found: {self.title}\n.")
            return
        self.books.remove(self.title)
        self.save

    def showbook(self):
        if not self.books:
            print("No books in library.\n")
            return
        for self.title in self.books:
            fname = f"{self.title}.txt"
            print(f"TITLE : {self.title}")
            try:
                with open(fname, 'r', encoding='utf-8') as f:
                    for line in f:
                        print(line.strip())
            except FileNotFoundError:
                print("(Book file missing!)")
            print()