import datetime


class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__OnLoad = False
        self.__DueDate = datetime.date.today()

    def GetTitle(self):
        return self.__Title

    def Borrowing(self):
        self.__OnLoad = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoad = False

    def PrintDetails(self):
        print(self.__Title, "; ", self.__Author__Artist, "; ", end="")
        print(self.__ItemID, "; ", self.__OnLoad, "; ", self.__DueDate)


class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0

    def GetIsRequested(self):
        return self.__IsRequested

    def SetIsRequested(self):
        self.__IsRequested = True


class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""

    def __GetGenre(self):
        return self.__Genre

    def SetGenre(self, g):
        self.__Genre = g


Book1 = Book("An Apple", "Alan", "7355608")
print(Book1.GetTitle())
Book1.Borrowing()
Book1.PrintDetails()
Book1.Returning()
Book1.PrintDetails()
