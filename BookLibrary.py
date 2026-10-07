class Book:
    """Represents a unique  book title in the system."""
    def __init__(self,title,author,copies):
      
        self.title=title
        self.author= author
        self.__copies= copies

        self.__total_copies= copies
        
    @property    
    def copies(self):
        return self.__copies
    @copies.setter    
    def copies(self,values):
        if 00<=  values >=self.__total_copies:
            self.__copies = values
    def add_more_copies(self,ount):
        self.__copies+=count
        self.__total_copies +=  count
    def is_loaned_out(self):
        return self.__copies < self.__total_copies
        
    def __str__(self):
        return f"'{self.title}' by'{self.author}'(copies Available : {self.__copies}/{self.__total_copies}"    
        

class Library:
    """Represents a specific Library branches that manages it  s  own physical inventory."""    
    
    def __init__(self):
        self.books= {}
        
       
    def add_book(self,title,author,copies):
        title= title.strip()
        if title in self.books:
            self.books[title].copies += copies
            print(f"updaated: added {copies} more copies to {title}")
        else:
            new_book=Book(title,author,copies)
            self.books[title] = new_book
            print(f"Success new entry  created for {title}")
       
           
    def show_all_book(self):
        
        if not self.books:
            print("there are no book available in this library")
            return 
        print("\n --- library Catalog---")   
        for book in self.books.values() :
            print(f"book_Details:{book}")
        #print("-" *40)
    def borrow_book(self,title):
        title = title.strip()
        if title not in self.books:
            print(f" Error:{title}'is not in the Library system")
            return 
            
        book = self.books[title]
        if book.copies >0:
            book.copies-=1
            print("\n---- Borrowing_Details---")
            print(f"Successs: you borrowed {title} (remaining books : {book.copies})")
        else:
            print(f"No copies of {title} are currently  Aailable")
            
    def return_book(self,title):
          title = title.strip()
          if title not in self.books:
            print(f" Error:{title}'does not belong to this Library")
            return
              
          book = self.books[title]
          if book.is_loaned_out():
             book.copies+= 1
             print(f"Success, thank you for returning book {title}")

          else :
              print(f"Refuesd: All copies of {title} are already on the shelves. Nothing out of loan.")
          
if __name__ == "__main__" :
    b=Book("Applied crypto Science","Dr.Mahesh kumar",26)
    l = Library()
    l.add_book("Secret Cryptography","Rajkumar",120)
    l.add_book("Applied crypto Science","Dr.Mahesh kumar",26)
    l.add_book("An intro to  AI","smt. Nidhi",425)
    l.show_all_book()
    l.borrow_book("Applied crypto Science")
    l.borrow_book("Applied crypto Science")
    l.borrow_book("Secret Cryptography")
    l.show_all_book()
    l.return_book("Secret Cryptography")

