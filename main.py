import sys


class Book:
    def __init__(self):
        Id: int
        Title: str
        Author: str
        Description: str

    def viewAllBooks():
        myfile = open("Database.txt", "r")
        mylist = myfile.readlines()
        print(mylist)
        myfile.close()

    def addBook(bookInfo):
        lineNumber = 1
        with open('Database.txt', 'r') as readObject:
         for line in readObject:
            lineNumber = lineNumber+1
        myfile = open('Database.txt', 'a')
        myfile.write('\n')
        myfile.write(str(lineNumber))
        for item in bookInfo:
          myfile.write('\t')
          myfile.write(item)
        myfile.close()
        print('Book inserted successfully')

    def searchForBook(keyValue):
        lineNumber = 0
        listOfResults = []
        with open('Database.txt', 'r') as readObject:
         for line in readObject:
            lineNumber += 1
            if keyValue in line:
                listOfResults.append((lineNumber, line.rstrip()))
         print('the following line matches this keyword')
         for item in listOfResults:
            print (item)


    def editBook(bookId,bookTitle,bookAuthor,bookDescription):
        lineNumber = 0
        with open('Database.txt', 'r') as readObject:
            for line in readObject:
                lineNumber += 1
                if bookId in line:
                    line = line.strip()
                    writeFile = open('Database.txt','w')
                    writeFile.line.write(bookId,bookTitle,bookAuthor,bookDescription)
                    writeFile.close()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        print('Welcome to book Application');
        print('1) View all books')
        print('2) add book')
        print('3) edit book')
        print('4) search for book')
        print('5) save and Exit')
        print('choose [1-5]')
        input1 = input()

        if input1 == '1':
            Book.viewAllBooks()

        if input1 == '2':
            bookInfo= []
            print('Title: ')
            bookInfo.append(input())
            print('Author :')
            bookInfo.append(input())
            print('Description :')
            bookInfo.append(input())
            Book.addBook(bookInfo)

        if input1 == '3':
            Book.viewAllBooks()
            print('Enter the book ID of the book you want to edit; to return press <Enter>')
            bookId = input()
            print('Input the following information. To leave a field unchanged, hit <Enter>')
            print('Title: ')
            bookTitle=input()
            print('Author :')
            bookAuthor= input()
            print('Description :')
            bookDescription = input()
            Book.editBook(bookId,bookTitle,bookAuthor,bookDescription)

            if input1 == '4':
                print('Type in one or more keywords to search for')
                searchvlaue = input()
                Book.searchForBook(searchvlaue)

            if input1 == '5':
                sys.exit



