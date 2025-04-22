class book():
    def __init__(self):
        self.name = "Tjay"
        self.title = "T"


    def Add(self):
        self.title = input("What book would you like to read?")
        print("you have added", self.title)