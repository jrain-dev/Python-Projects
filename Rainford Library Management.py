#Rainford Library Management

class Data:
    books = {    
        1: {'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian', 'available': True},
        2: {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Fiction', 'available': True},
        3: {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Classic', 'available': True},
        4: {'title': 'Moby-Dick', 'author': 'Herman Melville', 'genre': 'Adventure', 'available': True},
        5: {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'genre': 'Romance', 'available': True},
        6: {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'genre': 'Fiction', 'available': True},
        7: {'title': 'Crime and Punishment', 'author': 'Fyodor Dostoevsky', 'genre': 'Psychological Fiction', 'available': True},
        8: {'title': 'The Odyssey', 'author': 'Homer', 'genre': 'Epic Poetry', 'available': True},
        9: {'title': 'War and Peace', 'author': 'Leo Tolstoy', 'genre': 'Historical Fiction', 'available': True},
        10: {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'genre': 'Fantasy', 'available': True},
        11: {'title': 'Brave New World', 'author': 'Aldous Huxley', 'genre': 'Dystopian', 'available': True},
        12: {'title': 'The Chronicles of Narnia', 'author': 'C.S. Lewis', 'genre': 'Fantasy', 'available': True},
        13: {'title': 'Fahrenheit 451', 'author': 'Ray Bradbury', 'genre': 'Dystopian', 'available': True},
        14: {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'genre': 'Fantasy', 'available': True},
        15: {'title': 'Frankenstein', 'author': 'Mary Shelley', 'genre': 'Gothic', 'available': True},
        16: {'title': 'Dracula', 'author': 'Bram Stoker', 'genre': 'Gothic Horror', 'available': True},
        17: {'title': 'The Picture of Dorian Gray', 'author': 'Oscar Wilde', 'genre': 'Philosophical Fiction', 'available': True},
        18: {'title': 'Anna Karenina', 'author': 'Leo Tolstoy', 'genre': 'Historical Fiction', 'available': True},
        19: {'title': 'The Bell Jar', 'author': 'Sylvia Plath', 'genre': 'Autobiographical Fiction', 'available': True},
        20: {'title': 'Catch-22', 'author': 'Joseph Heller', 'genre': 'Satire', 'available': True},
        21: {'title': 'Slaughterhouse-Five', 'author': 'Kurt Vonnegut', 'genre': 'Science Fiction', 'available': True},
        22: {'title': 'Beloved', 'author': 'Toni Morrison', 'genre': 'Historical Fiction', 'available': True},
        23: {'title': 'The Road', 'author': 'Cormac McCarthy', 'genre': 'Post-apocalyptic Fiction', 'available': True},
        24: {'title': 'The Brothers Karamazov', 'author': 'Fyodor Dostoevsky', 'genre': 'Philosophical Novel', 'available': True},
        25: {'title': 'The Handmaid\'s Tale', 'author': 'Margaret Atwood', 'genre': 'Dystopian', 'available': True},
        26: {'title': 'The Sun Also Rises', 'author': 'Ernest Hemingway', 'genre': 'Modernist Fiction', 'available': True},
        27: {'title': 'Wuthering Heights', 'author': 'Emily Brontë', 'genre': 'Gothic Fiction', 'available': True},
        28: {'title': 'The Great Divorce', 'author': 'C.S. Lewis', 'genre': 'Christian Allegory', 'available': True},
        29: {'title': 'The Scarlet Letter', 'author': 'Nathaniel Hawthorne', 'genre': 'Historical Fiction', 'available': True},
        30: {'title': 'Jane Eyre', 'author': 'Charlotte Brontë', 'genre': 'Gothic Fiction', 'available': True},
        31: {'title': 'The Grapes of Wrath', 'author': 'John Steinbeck', 'genre': 'Historical Fiction', 'available': True},
        32: {'title': 'Lord of the Flies', 'author': 'William Golding', 'genre': 'Allegorical Fiction', 'available': True},
        33: {'title': 'Invisible Man', 'author': 'Ralph Ellison', 'genre': 'Literary Fiction', 'available': True},
        34: {'title': 'The Outsiders', 'author': 'S.E. Hinton', 'genre': 'Young Adult Fiction', 'available': True},
        35: {'title': 'The Kite Runner', 'author': 'Khaled Hosseini', 'genre': 'Historical Fiction', 'available': True},
        36: {'title': 'Don Quixote', 'author': 'Miguel de Cervantes', 'genre': 'Novel', 'available': True},
        37: {'title': 'A Tale of Two Cities', 'author': 'Charles Dickens', 'genre': 'Historical Fiction', 'available': True},
        38: {'title': 'The Secret Garden', 'author': 'Frances Hodgson Burnett', 'genre': 'Children\'s Literature', 'available': True},
        39: {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'genre': 'Fiction', 'available': True},
        40: {'title': 'The Hunger Games', 'author': 'Suzanne Collins', 'genre': 'Dystopian', 'available': True},
        41: {'title': 'The Shining', 'author': 'Stephen King', 'genre': 'Horror', 'available': True},
        42: {'title': 'The Fault in Our Stars', 'author': 'John Green', 'genre': 'Young Adult Fiction', 'available': True},
        43: {'title': 'The Giver', 'author': 'Lois Lowry', 'genre': 'Dystopian', 'available': True},
        44: {'title': 'A Brief History of Time', 'author': 'Stephen Hawking', 'genre': 'Non-fiction', 'available': True},
        45: {'title': 'The Girl with the Dragon Tattoo', 'author': 'Stieg Larsson', 'genre': 'Mystery', 'available': True},
        46: {'title': 'The Godfather', 'author': 'Mario Puzo', 'genre': 'Crime Fiction', 'available': True},
        47: {'title': 'The Hitchhiker\'s Guide to the Galaxy', 'author': 'Douglas Adams', 'genre': 'Science Fiction', 'available': True},
        48: {'title': 'The Book Thief', 'author': 'Markus Zusak', 'genre': 'Historical Fiction', 'available': True},
        49: {'title': 'Gone with the Wind', 'author': 'Margaret Mitchell', 'genre': 'Historical Fiction', 'available': True}
    }

    users = {
        1: {'name': 'Jordan', 'borrowed_books': []},
        2: {'name': 'Jaidon', 'borrowed_books': []},
        3: {'name': 'Diane', 'borrowed_books': []},
        4: {'name': 'Marvin', 'borrowed_books': []}
    }

class Library:
    def __init__(self):
        self.d = Data()

    def borrowBook(self, user_id, book_id):
        if self.d.books[book_id]['available']:
            self.d.books[book_id]['available'] = False
            self.d.users[user_id]['borrowed_books'].append(book_id)
            print(f"You're now borrowing {self.d.books[book_id]['title']}.")
        else:
            print(f"Sorry, {self.d.books[book_id]['title']} is checked out right now.")
    
    def returnBook(self, user_id, book_id):
        if self.d.books[book_id]['available']:
            self.d.books[book_id]['available'] = True
            self.d.users[user_id]['borrowed_books'].remove(book_id)
            print(f"You successfully returned {self.d.books[book_id]['title']}, Thank You!")

    def addBook(self):
        title = input("What is the name of the book? ")
        author = input("What is the name of the author? ")
        genre = input("What is the genre of the book? ")

        book_id = len(self.d.books) + 1  
    
        self.d.books[book_id] = {'title': title, 'author': author, 'genre': genre, 'available': True}
        
        print(f"Youve successfully added {self.d.books[book_id]['title']} to our library, Thank You!")
   
    def viewBooks(self):
        print("\nList of Books:")
        for book_id, book_details in self.d.books.items():
            print(f"ID: {book_id} | Title: {book_details['title']} | Author: {book_details['author']} | Genre: {book_details['genre']} | Available: {'Yes' if book_details['available'] else 'No'}")

    def searchAll(self, query):
        tags = query.split()
        results = []

        for book_id, book_details, in self.d.books.items():
            for tag in tags:
                if (tags in book_details['title'].lower() or
                        tags in book_details['author'].lower() or
                        tags in book_details['genre'].lower()):
                        results.append(book_details)
                        break

        if results:
            print("\nSearch Results:")
            for result in results:
                print(f"ID: {book_id} | Title: {book_details['title']} | Author: {book_details['author']} | Genre: {book_details['genre']} | Available: {'Yes' if book_details['available'] else 'No'}")
        else:
            print("No books found matching your search.")

    def searchGenres(self, query):
        tags = query.split()
        results = []

        for book_id, book_details, in self.d.books.items():
            for tag in tags:
                if (tags in book_details['genre'].lower()):
                    results.append(book_details)
                    break

        if results:
            print("\nSearch Results:")
            for result in results:
                print(f"ID: {book_id} | Title: {book_details['title']} | Author: {book_details['author']} | Genre: {book_details['genre']} | Available: {'Yes' if book_details['available'] else 'No'}")
                

    def searchAuthors(self, query):
        tags = query.split()
        results = []

        for book_id, book_details, in self.d.books.items():
            for tag in tags:
                if (tags in book_details['author'].lower()):
                    results.append(book_details)
                    break

        if results:
            print("\nSearch Results:")
            for result in results:
                print(f"ID: {book_id} | Title: {book_details['title']} | Author: {book_details['author']} | Genre: {book_details['genre']} | Available: {'Yes' if book_details['available'] else 'No'}")
                
    def main(self):
        print("Welcome to the Rainford Domestic Library System!")
        while True:
            userchoice = int(input("--------Menu--------\n"
                  "1) Add a Book\n"
                  "2) Borrow a Book\n"
                  "3) Return a Book\n"
                  "4) Search Options\n"
                  "5) Exit\n"))
            
            if userchoice == 1:
                self.addBook()

            elif userchoice == 2:
                self.borrowBook()

            elif userchoice == 3:
                self.returnBook()

            elif userchoice == 4:
                displaychoice = int(input("-----Search Menu-----\n"
                  "1) Filter by Genre\n"
                  "2) Filter by Author\n"
                  "3) Search All Books\n"
                  "4) View All Books\n"
                  "5) Go Back\n"))
                
                if displaychoice == 1:
                    query = input("Enter Genre(s): ").lower()
                    self.searchGenres

                if displaychoice == 2:
                    query = input("Enter Author(s): ").lower()
                    self.searchAuthors(query)

                if displaychoice == 3:
                    query = input("Enter Title, Author, or Genre: ").lower()
                    self.searchAll()
                
                if displaychoice == 4:
                    self.viewBooks()

                elif userchoice == 5:
                    break

            elif userchoice == 5:
                break
            
            else:
                print("Please input a valid menu item")

Library().main()


