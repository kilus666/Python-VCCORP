import sqlite3
import pickle
class Files:
    @classmethod
    def saveID1(cls):
        with open("ID1.pickle","wb") as I1:
            pickle.dump(ID.catID, I1)
    @classmethod
    def readID1(cls):
        with open("ID1.pickle","rb") as I1:
            ID.catID= pickle.load(I1)
    @classmethod
    def saveID(cls):
        with open("ID.pickle","wb") as I:
            pickle.dump(ID.lastID, I)
    @classmethod
    def readID(cls):
        with open("ID.pickle","rb") as I:
            ID.lastID= pickle.load(I)
    @classmethod
    def saveFile(cls):
        conn= sqlite3.connect("Bookstore.db")
        c= conn.cursor()
        try: 
            c.execute("Create Table listBook (ID, Name, Amount, Price,Cost)")
        except Exception:
            pass
        conn.commit()

        for key, value in book.bookList.items():
            name= value.name
            amount= value.amount
            price= value.price
            cost= value.cost
            ID= value.id
            with conn:
                c= conn.cursor()
                c.execute("""Insert Into book Values(:ID, :Name, :Amount, :Price,:Cost"""
                , {"ID": ID, "Name":name, "Amount": amount, "Price": price, "Cost":cost })
                
                        
    @classmethod
    def readfile(cls):

        with open("Inventory.pickle", "rb") as inven:
            book.bookList= pickle.load(inven)

        with open("Category.pickle", "rb") as cate:
            category.CategoryList= pickle.load(cate)

        with open("CatId.pickle", "rb") as catid:
            category.IdList= pickle.load(catid)

        with open("bookID.pickle", "rb") as bookID:
            book.Idlist= pickle.load( bookID)
class ID:
    lastID= 0
    catID= 0
    @classmethod
    def setid(cls):
        try:
            Files.readID()
        except Exception:
            pass
        cls.lastID+=1
        Files.saveID()
        return cls.lastID
    
    @classmethod
    def setid1(cls):
        try:
            Files.readID1()
        except Exception:
            pass
        cls.catID+=1
        Files.saveID1()
        return cls.catID

class book:
    Idlist={}
    bookList= {}
    def __init__(self, name, amount, cost, price, categoryID=None):
        self.id= None
        self.name= name
        self.category= categoryID
        self.amount= amount
        self.cost=cost
        self.price= price
    @classmethod
    def addBook(cls,book):
        book.id= ID.setid()
        cls.bookList[book.id]= book
        cls.Idlist[book.name]=[book.id]

Book1= book('a', 12,3,4)
Book2= book('b', 12,3,4)
Book3= book('c', 12,3,4)

book.addBook(Book1)
book.addBook(Book2)
book.addBook(Book3)

conn= sqlite3.connect("Bookstore.db")
c= conn.cursor()
try:
    c.execute("""CREATE TABLE book(
                ID integer PRIMARY KEY,
                Name text,
                Amount integer,
                Price real,
                Cost real
    )""")
except Exception:
    pass

try:
    c.execute("""CREATE TABLE IdMergeCat(
                ID integer 
                CatID integer
    )""")
except Exception:
    pass


try:
    c.execute("""CREATE TABLE Category(
                CatID integer PRIMARY KEY,
                Name text,
                Parent text
    )""")
except Exception:
    pass

def SaveToSqlite():
    for key, value in book.bookList.items():
        name= value.name
        amount= value.amount
        price= value.price
        cost= value.cost
        ID= value.id
        with conn:
            c.execute("""Insert Into book Values(:ID, :Name, :Amount, :Price,:Cost)"""
                        , {"ID": ID, "Name":name, "Amount": amount, "Price": price, "Cost":cost })
            conn.commit()

        # for i in value.category:
        #     with conn:
        #         c.execute("Insert Into IdMergeCat(:ID, :CategoryID)", {"ID":value.id, "CategoryID": i})
        #         conn.commit()
    
    # for key, value in category.bookList.items():
    #     CategoryID= value.id
    #     name= value.name
    #     parent= value.parent
    #     with conn:
    #         c.execute("Insert Into Category Values(:CategoryID,:Name, :Parent)",{"Category": CategoryID, "Name": name,"Parent":parent})
    #         conn.commit()

def readFromSqlite():
    # For book.bookList
    c.execute("Select * From book")
    while c.fetchone()!=None:
        info= c.fetchone()
        try:
            book.bookList[info[0]]= book(info[1],info[2],info[3],info[4])
        except TypeError:
            pass
     

    
    conn.close()
# SaveToSqlite()
readFromSqlite()
for i, j in book.bookList.items():
    print(i, j.name)