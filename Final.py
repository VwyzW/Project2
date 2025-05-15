class book():
    def __init__(self):
        self.index_file = 'index.txt'
        
        try:
            with open(self.index_file, 'r', encoding='utf-8') as f:
                self.title = [line.strip().upper() for line in f if line.strip()]
        except FileNotFoundError:
            with open (self.index_file, 'w', encoding='utf-8'):
                pass
            self.titles = []

    def save(self):
        with open(self.index_file, 'w',encoding='utf-8') as f:
            for t in self.titles:
                f.write(t + '\n')

    def Add(self):
        title = input("Enter the name of the book you add: \n").strip().upper()
        if title in self.title :
            print(f"Book '{title}' already exists.\n")
            return
        self.author = input("Enter the author of the book you add: \n").strip()
        try:
            self.price = float(input("Enter the listing price the book: \n"))
        except ValueError:
            print("The price format is incorrect, failed to add。")
            return
        fname = f"{title}.txt"
        with open(fname, 'w' , encoding='uutf-8') as f:
            f.write(f"author: {self.author}\n")
            f.write(f"price: {self.price}\n")
        
        self.titles.append(title)
        self.save
        print(f"you have added {title}.\n")
        
    def Minus(self):
        title = input("enter the name of the bookyou remove: \n").strip().upper()
        if title not in self.Books:
            print(f"Book not found: {title}\n")
            return
        self.titles.append(title)
        self.save()

    def showbook(self):
        if not self.titles:
            print("No books in library.\n")
            return
        for title in self.titles():
            fname = f"{title}.txt"
            print(f"TITLE : {title}")
            try:
                with open(fname, 'r', encoding='utf-8') as f:
                    for line in f:
                        print(line.strip())
            except FileNotFoundError:
                print("(Book file missing!)")
            print()