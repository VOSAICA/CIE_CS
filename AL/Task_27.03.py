import datetime


class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__OnLoad = False
        self.__DueDate = datetime.date.today()
        self.__BorrowerID = 0

    def GetTitle(self):
        return self.__Title

    def Borrowing(self, BorrowerID):
        self.__OnLoad = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
        self.__BorrowerID = BorrowerID

    def Returning(self, BorrowerID):
        self.__OnLoad = False
        self.__BorrowerID = BorrowerID

    def PrintDetails(self):
        print(self.__Title, "; ", self.__Author__Artist, "; ", end="")
        print(self.__ItemID, "; ", self.__OnLoad, "; ", self.__DueDate)


class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = []

    def __newRequest(self, BorrowerID):
        self.__RequestedBy.append(str(BorrowerID))

    def GetIsRequested(self):
        print(self.__RequestedBy)
        return self.__IsRequested

    def SetIsRequested(self, BorrowerID):
        self.__IsRequested = True
        self.__newRequest(BorrowerID)

    def PrintDetails(self):
        super(Book, self).PrintDetails()
        print(self.__IsRequested)


class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""

    def GetGenre(self):
        return self.__Genre

    def SetGenre(self, g):
        self.__Genre = g

    def PrintDetails(self):
        super(CD, self).PrintDetails()
        print(self.__Genre)


class Borrower:
    def __init__(self, Name, Email, ID):
        self.__BorrowerName = Name
        self.__EmailAddress = Email
        self.__BorrowerID = ID
        self.__ItemsOnLoan

    def GetBorrowerName(self):
        return self.__BorrowerName

    def GetEmailAddress(self):
        return self.__EmailAddress

    def GetBorrowerID(self):
        return self.__BorrowerID

    def GetItemsOnLoan(self):
        return self.__ItemsOnLoan

    def PrintDetails(self):
        print(self.__BorrowerName, "; ", self.__EmailAddress, "; ", end="")
        print(self.__BorrowerID, "; ", self.__ItemsOnLoan.GetTitle())


Book1 = Book("An Apple", "Alan", "7355608")
Book1.Borrowing(23456)
Book1.PrintDetails()
Book1.SetIsRequested(56789)
Book1.GetIsRequested()

Borrower1 = Borrower("Brown", "Brown@gmail.com", "114514", Book1)
Borrower1.PrintDetails()
