class book():
    def __init__(self):
        self.name = "Tjay"
        self.title = "T"
        self.price = 0
        self.Book = {}


    def Add(self):
        self.title = input("enter the name of the book you add: \n").upper
        self.author = input("enter the author of the book you add: \n").upper
        self.price = float(input("Enter the listing price the book: \n"))


        self.Book[self.title] = {'Auther':self.author, 'price':self.price}
        print(self.Book)
