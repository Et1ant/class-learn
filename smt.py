class Book:
    def __init__(self, title, author, year):
        self.title     = title
        self.author    = author
        self.year      = year
        self.available = True

    def __str__(self):
        status = "доступна" if self.available else "выдана"
        return f"{self.title} ({self.author}, {self.year}) — {status}"
class LibraryItem(Book):
    def __init__(self, title, author, year, id):
        super().__init__(title, author, year)
        self.item_id = id
    def get_info(self):
        return f"[ID {self.item_id}] {self}"
class Library:
    total_books = 0    
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        Library.total_books += 1
    def find_by_author(self, author):
        return [b for b in self.books
                if b.author == author and b.available]
    def checkout(self, item_id):
        for b in self.books:
            if b.item_id == item_id:
                b.available = False
                print(f"Выдана: {b.title}")
                return
    def return_book(self, item_id):
        for b in self.books:
            if b.item_id == item_id:
                b.available = True
                print(f"Возвращена: {b.title}")
                return
lib = Library()
lib.add_book(LibraryItem("Мастер и Маргарита", "Булгаков", 1967, id=1))
lib.add_book(LibraryItem("1984", "Оруэлл", 1949, id=2))
lib.add_book(LibraryItem("Собачье сердце", "Булгаков", 1925, id=3))
lib.checkout(1)
lib.checkout(2)
lib.return_book(1)
bulgakov = lib.find_by_author("Булгаков")
for b in bulgakov:
    print(b)
print("Всего книг добавлено:", Library.total_books)