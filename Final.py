class book():
    def __init__(self):
        self.name = "Tjay"
        self.title = "T"
        self.price = 0
        self.book = {}


    def Add(self):
        self.title = input("enter the name of the book you add: \n").upper
        self.author = input("enter the author of the book you add: \n").upper
        self.price = float(input("Enter the listing price the book: \n"))

        print("you have added", self.title)
        print(self.book)

def Muins(self):
    self.title = input("enter the name of the bookyou remove: \n")
    try:
        str(self.title)
        if self.title in self.book:
            del self.book[self.title]
            print(self.book)

    except:
        print("Please enter a book title")



def showbook(self):
    for x in self.book:
        print(x)
        print(self.book[x]["aother"])
        print(self.book[x]["price"])
