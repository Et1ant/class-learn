from typing import List, Optional
class Book:
    """Базовый класс книги."""
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
    def __str__(self) -> str:
        status = "в наличии" if self.is_available else "выдана"
        return f"«{self.title}» | {self.author} ({self.year}) — {status}"
class LibraryItem(Book):
    """Книга, привязанная к инвентарю библиотеки."""
    def __init__(self, title: str, author: str, year: int, item_id: int):
        super().__init__(title, author, year)
        self.id = item_id
class Library:
    """Управление фондом библиотеки."""
    def __init__(self):
        self.catalog: List[LibraryItem] = []
    def add_book(self, book: LibraryItem):
        self.catalog.append(book)
        print(f"[+] Добавлено: {book.title}")
    def find_book(self, item_id: int) -> Optional[LibraryItem]:
        """Ищет книгу в каталоге по ID."""
        for book in self.catalog:
            if book.id == item_id:
                return book
        return None
    def checkout_book(self, item_id: int):
        """Выдает книгу читателю."""
        book = self.find_book(item_id)        
        if not book:
            print(f"[!] Ошибка: Книга с ID {item_id} не найдена.")
            return
        if book.is_available:
            book.is_available = False
            print(f"[→] Выдана: {book.title}")
        else:
            print(f"[!] Ошибка: {book.title} уже на руках.")
    def return_book(self, item_id: int):
        """Принимает книгу обратно."""
        book = self.find_book(item_id)       
        if book and not book.is_available:
            book.is_available = True
            print(f"[←] Возвращена: {book.title}")
        else:
            print(f"[!] Ошибка: Невозможно вернуть книгу с ID {item_id}.")
if __name__ == "__main__":
    library = Library()
    # Наполняем библиотеку
    library.add_book(LibraryItem("Мастер и Маргарита", "М. Булгаков", 1967, 101))
    library.add_book(LibraryItem("1984", "Дж. Оруэлл", 1949, 102))
    print("-" * 30)
    library.checkout_book(101)
    library.checkout_book(101)  
    library.return_book(101)    
    print("-" * 30)
    for item in library.catalog:
        print(item)