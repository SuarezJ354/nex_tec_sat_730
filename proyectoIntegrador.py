""" Proyecto biblioteca """
def Libros():
    def __init__ (self, titulo, autor, año, genero):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.genero = genero
    def mostrar_datos(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.año}, Género: {self.genero}"

books = {}
def Library ():
    book = []
    
    def agregar_libro(libro):
        tittle = input("Ingrese el titulo del libro ")
        book.append(tittle)
        autor = input("Ingrese el nombre del autor del libro ")
        book.append(autor)
        yearBook = input("Ingrese el año de lanzamiento del libro ")
        book.append(yearBook)
        genre = input("Ingrese el genero del libro ")
        book.append(genre)
        books.update(book)
        
    def DeleteBook():
        book.pop()
        print("Libro eliminado")
        return books
    def SearchBooks ():
        search_title = input("Ingrese el título del libro: ")
        for book in books:
            if book.title == search_title:
                return book.mostrar_datos()
        print("Libro no encontrado")
    
    def ListBooks ():
        for book in books:
            print(book.mostrar_datos())
            print("---")
            return books
        print("No hay libros en la biblioteca")
        return books
    return {
        'Libros': books,
        'Agregar_libro': agregar_libro,
        'DeleteBook': DeleteBook,
        'SearchBooks': SearchBooks,
        'ListBooks': ListBooks
        }



def menu_principal ():
    library = Library()

    while
