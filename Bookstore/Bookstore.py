import time
import sqlite3
import pickle
import pandas as pd
import schedule

class generateID:
    bookID= 0
    categoryID= 0
    
    
    @classmethod
    def setBookID(cls):
        try:
            File.readID()
        except Exception:
            pass
        cls.bookID+=1

        File.saveID()
        
    
    @classmethod
    def setCategoryID(cls):
        try:
            File.readID()
        except Exception:
            pass
        cls.categoryID+=1
        
        File.saveID()
 
class File:
    @classmethod
    def saveID(cls):
        with open("BookID.pickle", "wb") as BID:
            pickle.dump(generateID.bookID, BID)
        with open("CategoryID.pickle","wb") as CatID:
            pickle.dump(generateID.categoryID,CatID)
    @classmethod
    def readID(cls):
        with open("BookID.pickle", "rb") as BID:
            generateID.bookID= pickle.load(BID)
        with open("CategoryID.pickle","rb") as CatID:
            generateID.categoryID= pickle.load(CatID)

class Sqlite:
    @classmethod
    def createDataBase(cls):
        conn= sqlite3.connect("BookStore.db")
        with conn:
            c= conn.cursor()
            try:
                c.execute("""Create Table BookTable(
                                BookID integer Primary Key NOT NULL,
                                Name text NOT NULL,
                                Amount integer NOT NULL,
                                Price real,
                                Cost real                           
                            )""")
                conn.commit()
            except Exception:
                pass

            try:
                c.execute("""Create Table CategoryTable(
                                CategoryID integer Primary Key NOT NULL,
                                Name text NOT NULL,
                                Parent text
                            )""")
                conn.commit()
            except Exception:
                pass

            try:
                c.execute("""Create Table BookCategory(
                                BookID integer NOT NULL,
                                CategoryID integer NOT NULL
                            )""")
                conn.commit()
            except Exception:
                pass
    
    @classmethod           
    def loadBookLibrary(cls):
        conn= sqlite3.connect("BookStore.db")
        with conn:
            c= conn.cursor()
            c.execute("Select* From BookTable")
            data=c.fetchall()
            pokemon= pd.DataFrame(data, columns=["ID","Name", "Amount", "Price", "Cost"])
            pokemon.set_index("ID", inplace= True)
            conn.commit()

            return pokemon
    
    @classmethod
    def loadBookCategory(cls):
        conn= sqlite3.connect("BookStore.db")
        with conn:
            c= conn.cursor()
            c.execute("Select* From BookCategory")
            data=c.fetchall()
            mewtwo= pd.DataFrame(data, columns=["BookID","CatID"])
            conn.commit()

            return mewtwo
          
    @classmethod
    def loadCategoryLibrary(cls):
        conn= sqlite3.connect("BookStore.db")
        with conn:
            c= conn.cursor()
            c.execute("Select* From CategoryTable")
            data=c.fetchall()
            pikachu= pd.DataFrame(data, columns=["CatID","Name", "Parent"])
            pikachu.set_index("CatID", inplace= True)
            return pikachu

class book:
    def __init__(self,name, category, amount, price, cost):
        self.Id= None
        self.name= name
        self.category= category
        self.amount= amount
        self.price= price
        self.cost = cost
 
    @classmethod
    def addBookHelper(cls, Book):
        generateID.setBookID()
        Book.Id= generateID.bookID
        
        Id= Book.Id
        name= Book.name
        category= Book.category
        amount= Book.amount
        price= Book.price
        cost= Book.cost
        
        conn= sqlite3.connect("BookStore.db")
        with conn:
                c= conn.cursor()
                c.execute("""INSERT INTO BookTable(BookID, Name, Amount, Price, Cost) VALUES(?,?,?,?,?)""", (Id, name, amount, price, cost))
                
                for i in category:
                    c.execute("""INSERT INTO BookCategory VALUES(?,?)""", (Id, i))
    @classmethod
    def editBookHelper(cls, Book):
        Id= Book.Id
        name= Book.name
        category= Book.category
        amount= Book.amount
        price= Book.price
        cost= Book.cost
        conn= sqlite3.connect("BookStore.db")
        with conn:
                c= conn.cursor()
                c.execute("""UPDATE BookTable
                SET Name= ?, Amount=?, Price=?, Cost=? 
                WHERE BookID= ?""", (name, amount, price, cost, Id))
                c.execute("""DELETE FROM BookCategory WHERE BookID= ?""",(Id,))
                for i in category:
                    c.execute("""INSERT INTO BookCategory  VALUES(?,?)""", (Id, i))
    
    @classmethod
    def delBookHelper(cls,bookID):
        Id= bookID
        conn= sqlite3.connect("BookStore.db")
        with conn:
                c= conn.cursor()
                c.execute|("""DELETE FROM BookTable WHERE BookID= Id""")
                c.execute("""DELETE FROM BookCategory WHERE BookID= Id""")
    
class category:
    def __init__(self,name, parent=None):
        self.Id= None
        self.name= name
        self.parent = parent
    
    @classmethod
    def addCategoryHelper(cls, Cat):
        generateID.setCategoryID()
        Cat.Id= generateID.categoryID
        Id= Cat.Id
        name= Cat.name
        parent= Cat.parent        
        conn= sqlite3.connect("BookStore.db")
        with conn:
                c= conn.cursor()
                c.execute("""INSERT INTO CategoryTable(CategoryID, Name, Parent) VALUES(?,?,?)""", (Id, name, parent))

    @classmethod
    def delCategoryHelper(cls,CategoryID):
        Id= CategoryID
        conn= sqlite3.connect("BookStore.db")
        with conn:
                c= conn.cursor()
                c.execute("""DELETE FROM Category WHERE CategoryID= Id""")
                c.execute("""DELETE FROM BookCategory WHERE CategoryID= Id""")
    
    @classmethod
    def editCategoryHelper(cls, category):
        Id= category.id
        name= category.name
        parent= category.category
     
        conn= sqlite3.connect("BookStore.db")
        with conn:
                c= conn.cursor()
                c.execute("""UPDATE CategoryTable
                SET Name= ?, Parent=?
                WHERE ID= ?""", (name, parent, Id))

class employee:
    def __init__(self, name, age, gender, phone=None):
        self.name= name
        self.age= age
        self.gender= gender
        self.phone= phone
    @classmethod
    def searchID(cls, lookupID):

        a= Sqlite.loadBookLibrary()
        BookInfo= a.loc[lookupID]
        return BookInfo
    @classmethod
    def searchIdHelper(cls,lookupID):
        print(" ")
        a= Sqlite.loadBookLibrary()
        print(a.loc[[lookupID], ["Name", "Amount", "Price","Cost"]])
        print("Category:")
        for i in cls.searchBookCategory(lookupID):
            print(i)


    @classmethod
    def searchName(cls, lookupName):
        a= Sqlite.loadBookLibrary()
        print(a.loc[a["Name"]==lookupName])

    @classmethod
    def searchCategoryID(cls, lookupCategoryID):
        a= Sqlite.loadCategoryLibrary()
        print(a.loc[[lookupCategoryID]])
    
    @classmethod
    def searchCategoryName(cls, lookupCategoryName):
        a= Sqlite.loadCategoryLibrary()
        print(a.loc[a["Name"]==lookupCategoryName])

    @classmethod
    def searchBookCategory(cls, lookupBookID):
        a= Sqlite.loadBookCategory()
        CategoriesOfBook= list(a.loc[a["BookID"]==lookupBookID,"CatID"])
        return CategoriesOfBook
    
    @classmethod
    def browseAllBook(cls):
        a= Sqlite.loadBookLibrary()
        print(a)

class seller(employee):

    def sellBookHelper(self, bookID, sellAmount):
        info1= employee.searchID(bookID)
        info2= employee.searchBookCategory(bookID)
        if int(info1[1])>=sellAmount:
            updatedName= info1[0]
            updatedAmount= int(info1[1])-sellAmount
            updatedPrice= info1[2]
            updatedCost= info1[3]
            updatedCategory= info2
            updatedBook= book(updatedName, updatedCategory, updatedAmount, updatedPrice, updatedCost)
            updatedBook.Id= bookID
            book.editBookHelper(updatedBook)
        else:
            print("Not enough book in stock")
    
class purchaser(employee):
    def purchaseOldBookHelper(self, bookID, purchasedAmount):
        info1= employee.searchID(bookID)
        info2= employee.searchBookCategory(bookID)
        updatedName= info1[0]
        updatedAmount= int(info1[1])+ purchasedAmount
        updatedPrice= info1[2]
        updatedCost= info1[3]
        updatedCategory= info2
        updatedBook= book(updatedName, updatedCategory, updatedAmount, updatedPrice, updatedCost)
        updatedBook.Id= bookID
        book.editBookHelper(updatedBook)

    def purchaseNewBookHelper(self, NewBook):
        book.addBookHelper(NewBook)

    def purchaseHelper(self,bookPurchase):
        a= employee.searchID(bookPurchase)
        if a!=None:
            self.purchaseOldBookHelper(bookPurchase.Id, bookPurchase.amount)
        else:
            self.purchaseNewBookHelper(bookPurchase)
    
    # def editBook(self,bookID)


Sqlite.createDataBase()
def test():
    Book1= book("a", [1,2,3], 12,12,4)
    Book2= book("b", [3,4,6], 12,12,4)
    Book3= book("c", [2,5,3], 12,12,4)


    Cat1= category("a",3)
    Cat2= category("b",3)
    Cat3= category("c",4)
    Cat4= category("d",None)
    Cat5= category("e",4)
    Cat6= category("f",None)

    category.addCategoryHelper(Cat1)
    category.addCategoryHelper(Cat2)
    category.addCategoryHelper(Cat3)
    category.addCategoryHelper(Cat4)
    category.addCategoryHelper(Cat5)
    category.addCategoryHelper(Cat6)
    
    # print(Cat1.Id)
    # print(Cat2.Id)
    # print(Cat3.Id)
    # print(Cat4.Id)
    # print(Cat5.Id)
    # print(Cat6.Id)

    book.addBookHelper(Book1)
    book.addBookHelper(Book2)
    book.addBookHelper(Book3)
    # print(Book1.Id)
    # print(Book2.Id)
    # print(Book3.Id)

# test()
