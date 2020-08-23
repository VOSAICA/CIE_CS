from Package import *

BorrowerList = []
BookList = []
CDList = []


def findBorrower(borrowerID):
    for i in range(len(BorrowerList)):
        if BorrowerList[i].GetBorrowerID() == borrowerID:
            return int(i)


def operatingMenu():
    while True:
        print("1 - Add a new borrower")
        print("2 - Add a new book")
        print("3 - Add a new CD")
        print("4 - Borrow a book")
        print("5 - Return a book")
        print("6 - Borrow a CD")
        print("7 - Return a CD")
        print("8 - Request a book")
        print("9 - Print all details")
        print("99 - Exit Program")

        Choice = int(input("Enter your menu choice: "))

        if Choice == 1:
            newBorrower = Borrower(input("Name: "), input("Email: "), int(input(
                "ID: ")))
            BorrowerList.append(newBorrower)

        elif Choice == 2:
            newBook = Book(input("Title: "), input(
                "Author: "), int(input("ItemID: ")))
            BookList.append(newBook)

        elif Choice == 3:
            newCD = CD(input("Title: "), input(
                "Author: "), int(input("ItemID: ")))
            newCD.SetGenre(input("Genre: "))
            CDList.append(newCD)

        elif Choice == 4:
            wantedID = input("ItemID: ")
            borrowerID = input("BorrowerID: ")
            for i in range(len(BookList)):
                ItemID = BookList[i].GetID()
                if ItemID == wantedID:
                    if not BookList[i].GetStatus():
                        BookList[i].Borrowing(borrowerID)
                        j = findBorrower(borrowerID)
                        BorrowerList[j].AddBorrowedItem(wantedID)
                        break
                    else:
                        print("No item in Library")

        elif Choice == 5:
            wantedID = input("ItemID: ")
            borrowerID = input("BorrowerID: ")
            for i in range(len(BookList)):
                ItemID = BookList[i].GetID()
                if ItemID == wantedID:
                    if BookList[i].GetStatus() and BookList[i].GetBorrower() == borrowerID:
                        BookList[i].Returning(borrowerID)
                        break
                    else:
                        print("You have not borrowed this item")

        elif Choice == 6:
            wantedID = input("ItemID: ")
            borrowerID = input("BorrowerID: ")
            for i in range(len(CDList)):
                ItemID = CDList[i].GetID()
                if ItemID == wantedID:
                    if not CDList[i].GetStatus():
                        CDList[i].Borrowing(borrowerID)
                        j = findBorrower(borrowerID)
                        BorrowerList[j].AddBorrowedItem(wantedID)
                        break
                    else:
                        print("No item in Library")

        elif Choice == 7:
            wantedID = input("ItemID: ")
            borrowerID = input("BorrowerID: ")
            for i in range(len(CDList)):
                ItemID = CDList[i].GetID()
                if ItemID == wantedID:
                    if CDList[i].GetStatus() and CDList[i].GetBorrower() == borrowerID:
                        CDList[i].Returning(borrowerID)
                        break
                    else:
                        print("You have not borrowed this item")

        elif Choice == 8:
            requestID = input("ItemID: ")
            borrowerID = input("BorrowerID: ")
            for i in range(len(BookList)):
                ItemID = BookList[i].GetID()
                if ItemID == requestID:
                    BookList[i].SetIsRequested(borrowerID)
                    break

        elif Choice == 9:
            borrowerID = input("BorrowerID: ")
            i = int(findBorrower(borrowerID))
            BorrowerList[i].PrintDetails()

        elif Choice == 99:
            break

        else:
            print("Choose another number")


operatingMenu()
