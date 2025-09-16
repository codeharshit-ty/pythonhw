class library:
    def __init__(self,list_of_books,name):
        self.booklist = list_of_books
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"we have following books in library:{self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.booklist:
            print("sorry,we do not have that book.")
        elif book in self.lendDict:
            print(f"the book is already being used by{self.lendDict[book]}")
        else:
            self.lendDict[book] = user
            print(
                "lender-book database has been updated. you can take book now."
            )
    def  addbook(self,book):
        self.booklist.append(book)
        print(f"{book} has been added to the book list.")

    def returnbook(self,book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("book has been returned")
        else:
            print("that book wasn't borrowed from us .")
if __name__ == '__main__':
    books = library([
        'python','rich dad poor dad','harry potter','goosebumps 2','c++ basics'
    ],"let's upskill")
    user_name = input("welcome to our library! please enter your name:")
    while True:
        print(
f"\nHello {user_name}, welcome to the {books.name} library. Please choose an option:"
        )
        print("1. Display Books\n2. Lend a Book\n3. Add a Book\n4. Return a Book\n5. Quit")
        user_choice = input("Enter your choice to continue: ")
        if user_choice not in ['1', '2', '3', '4', '5']:
            print("please enter a valid option.")
            continue
        if user_choice == '1':
            books.displayBooks()
        elif user_choice == '2':
            book = input("Enter the name of the book you want to lend: ")
            books.lendBook(user_name, book)
        elif user_choice == '3':
            book = input("Enter the name of the book you want to add: ")
            books.addBook(book)
        elif user_choice == '4':
            book = input("Enter the name of the book you want to return: ")
            books.returnBook(book)
        elif user_choice == '5':
            print(f"Thank you for using the library, {user_name}. Goodbye!")
            break
