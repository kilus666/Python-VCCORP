import time
import sqlite3
import pickle
import pandas as pd
import schedule
from flask import Flask, jsonify, abort, make_response, request, render_template


class Sqlite:
    @classmethod
    def createDataBase(cls):
        conn= sqlite3.connect("BookStore.db")
        with conn:
            c= conn.cursor()
            try:
                c.execute("""Create Table BookTable(
                                BookID integer Primary Key,
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
                                CategoryID integer Primary Key,
                                Name text NOT NULL,
                                Parent text
                            )""")
                conn.commit()
            except Exception:
                pass

            try:
                c.execute("""Create Table BookCategory(
                                BookID integer NOT NULL,
                                CategoryID integer 
                            )""")
                conn.commit()
            except Exception:
                pass
class book:
    def __init__(self,name, amount, cost, price, category):
        self.Id= None
        self.name= name
        self.category= category
        self.amount= amount
        self.price= price
        self.cost = cost
 
    @classmethod
    def addBookHelper(cls, Book):

        name= Book.name
        category= Book.category
        amount= Book.amount
        price= Book.price
        cost= Book.cost
        
        conn= sqlite3.connect("BookStore.db")
        with conn:
                c= conn.cursor()
                c.execute("""INSERT INTO BookTable(Name, Amount, Price, Cost) VALUES(?,?,?,?)""", (name, amount, price, cost))
                if category is not None:
                    for i in category:
                        c.execute("Select Max(BookID) from BookTable")
                        maxID= c.fetchone()[0]
                        c.execute("""INSERT INTO BookCategory VALUES(?,?)""", (maxID, i))
                else:
                    c.execute("Select Max(BookID) from BookTable")
                    maxID= c.fetchone()[0]
                    c.execute("INSERT INTO BookCategory VALUES(?,?)",(maxID, None))
                
    
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
                c.execute("""DELETE FROM BookTable WHERE BookID= ?""",(Id,))
                c.execute("""I DELETE FROM BookCategory WHERE BookID=? """,(Id,))
    
class category:
    def __init__(self,name, parent=None):
        self.Id= None
        self.name= name
        self.parent = parent
    
    @classmethod
    def addCategoryHelper(cls, Cat):
        name= Cat.name
        parent= Cat.parent        
        conn= sqlite3.connect("BookStore.db")
        with conn:
                c= conn.cursor()
                c.execute("""INSERT INTO CategoryTable(Name, Parent) VALUES(?,?)""", (name, parent))

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
        conn= sqlite3.connect("BookStore.db")
        c= conn.cursor()
        with conn:
            c.execute("Select * From BookTable Where BookID= ?",(lookupID,))
            Info1= c.fetchone()

            c.execute("Select * From BookCategory Where BookID=?",(lookupID,))
            Info2= c.fetchall()
            if len(Info2)>0:
                bookCategory= {"Category": k[1] for k in Info2}                
                Book= {"id":Info1[0],"Name":Info1[1],"category":bookCategory, "amount":Info1[2],"price":Info1[3],"cost":Info1[4]}
                return Book
            else:
                Book= {"id":Info1[0],"Name":Info1[1],"category":None, "amount":Info1[2],"price":Info1[3],"cost":Info1[4]}
                return Book



    @classmethod
    def searchName(cls, lookupName):
        conn= sqlite3.connect("BookStore.db")
        c= conn.cursor()
        with conn:
            Books=[]
            c.execute("Select * From BookTable Where Name= ?",(lookupName,))
            all_records= c.fetchall()
            for i in all_records:
                c.execute("Select CategoryID from BookCategory Where BookID=?", (i[0],))
                book_categories= c.fetchall()
                book_categories= {"Category": i[0] for i in book_categories}
                Books.append({"BookID":i[0], "Name": i[1], "Category": book_categories, "Amount":i[2], "Price": i[3], "Cost": i[4]})
            return(Books)

    @classmethod
    def searchCategoryID(cls, lookupID):
        conn= sqlite3.connect("BookStore.db")
        c= conn.cursor()
        with conn:
            c.execute("Select * From CategoryTable Where CategoryID= ?",(lookupID,))
            Info1= c.fetchone()
            c.execute("Select * From BookCategory Where CategoryID=?",(lookupID,))
            Info2= c.fetchall()
            bookInCategory= {"Book": k[1] for k in Info2}
            Category= {"id":Info1[0],"Name":Info1[1],"List of books":bookInCategory, "Parent":Info1[2]}
            
            return Category
    
    @classmethod
    def searchCategoryName(cls, lookupName):
        conn= sqlite3.connect("BookStore.db")
        c= conn.cursor()
        with conn:
            Categories=[]
            c.execute("Select * From CategoryTable Where Name= ?",(lookupName,))
            all_records= c.fetchall()
            for i in all_records:
                book_in_category= c.execute("Select BookID From BookCategory Where CategoryID= ?",(i[0],))
                book_in_category= {"Book": j[0] for j in book_in_category}
                Categories.append({"Category ID":i[0], "Name": i[1], "List of books": book_in_category,"Parent":i[2]})
            return Categories

    
    @classmethod
    def allBook(cls):
            books=[]
            conn= sqlite3.connect("BookStore.db")
            with conn:
                c= conn.cursor()
                c.execute("Select * from BookTable")
                all_records= c.fetchall()
                for i in all_records:
                    c.execute("Select CategoryID from BookCategory Where BookID=?", (i[0],))
                    book_categories= c.fetchall()
                    book_categories= {"Category": i[0] for i in book_categories}
                    books.append({"BookID":i[0], "Name": i[1], "Category": book_categories, "Amount":i[2], "Price": i[3], "Cost": i[4]})
                    
            return books
    @classmethod
    def allCategories(cls):
        categories=[]
        conn= sqlite3.connect("BookStore.db")
        with conn:
            c= conn.cursor()
            c.execute("Select * from CategoryTable")
            all_records= c.fetchall()
            for i in all_records:
                c.execute("Select BookID From BookCategory Where CategoryID= ?",(i[0],))
                book_in_category= c.fetchall()
                book_in_category= {"Book": j[0] for j in book_in_category}
                categories.append({"Category ID":i[0], "Name": i[1], "List of books": book_in_category,"Parent":i[2]})
            return categories

class seller(employee):

    def sellBookHelper(self, bookID, sellAmount):
        conn= sqlite3.connect("BookStore.db")
        c= conn.cursor()
        with conn:
            c.execute("Select Amount,Price From BookTable WHERE BookID = ?",(bookID,))
            amount_price= c.fetchone()
            currentAmount, price= amount_price[0], amount_price[1]
            
            if currentAmount>=sellAmount:
                c.execute("""Update BookTable  
                        Set Amount=? Where BookID=?""",(currentAmount-sellAmount,bookID))
                try:
                    bills[bookID]+=(sellAmount*price)
                except KeyError:
                    bills[bookID]= sellAmount*price

    
    def sell_book_from_cart(self,books_in_cart):
        for bookID, amount in books_in_cart.items():
            a= self.sellBookHelper(bookID,amount)
            return bills
    
class purchaser(employee):

    def buy_book_helper(self, bookID, buyAmount):
        conn= sqlite3.connect("BookStore.db")
        c= conn.cursor()
        with conn:
            c.execute("Select Amount From BookTable WHERE BookID = ?",(bookID,))
            amount_price= c.fetchone()
            currentAmount= amount_price[0]
            
            c.execute("""Update BookTable  
                    Set Amount=? Where BookID=?""",(currentAmount+buyAmount,bookID))
            return "Successfully update the current item stock"

    def purchaseNewBookHelper(self, NewBook):
        book.addBookHelper(NewBook)


app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error":"not found"}))

@app.route("/", methods= ["GET"])
def search():
    return render_template("search.html")

@app.route("/book", methods= ["GET"])
def allBooks():
    a= employee.allBook()
    return jsonify("Books", a)


@app.route("/book/addtocart", methods=["POST"])
def add_book_to_cart():
    if not request.json or not "BookID" in request.json or not "Amount" in request.json:
        abort(404)
    else:
        BookID= request.json.get("BookID")
        sellAmount= request.json.get("Amount")
        try:
            shopping_cart[BookID]+= sellAmount
        except KeyError:
            shopping_cart[BookID]= sellAmount
        return "Successfully add to the cart"

@app.route("/book/addcurrent", methods=["PUT"])
def add_current_book():
    if not request.json or not "BookID" in request.json or not "Amount" in request.json:
        abort(404)
    else:
        BookID= request.json.get("BookID")
        buyAmount= request.json.get("Amount")
        purcharser1= purchaser("kyle",24,"male")
        a= purcharser1.buy_book_helper(BookID, buyAmount)
        return jsonify(a)

@app.route("/book/addnew", methods=["PUT"])
def add_new_book():
    if not request.json or not "BookName" in request.json or not "Amount" in request.json or not "Cost" in request.json:
        abort(404)
    else:
        book_name= request.json.get("BookName")
        Amount= request.json.get("Amount")
        Cost=request.json.get("Cost")
        Category= request.json.get("Category")
        price= request.json.get("Price")
        new_book= book(book_name,Amount,Cost,price,Category)
        book.addBookHelper(new_book)
        result= [{"Name": book_name, "Amount": Amount, "Cost": Cost, "Price": price, "Category": Category}]
        return jsonify("Successfully add the book", result)
    

@app.route("/category",methods=["GET"])
def allCategory():
    a= employee.allCategories()
    return jsonify("Category", a)

@app.route("/book/search", methods=["POST"])
def book_search_post():
    value= request.form.get("Name")
    results= bookSearch(value)
    return results

# @app.route("/book/search/<value>", methods= ["GET"])
# def bookSearch(value):
#     try:
#         a= employee.searchID(int(value))
#         return jsonify("Book", a)

#     except Exception:
#         a= employee.searchName(value)
#         if len(a)==0:
#             return abort(404)
#         return jsonify("Book", a)

@app.route("/book/search/<value>", methods= ["GET"])
def bookSearch(value):
    try:
        a= employee.searchID(int(value))
        return render_template("result.html", Book_Id= a)

    except Exception:
        a= employee.searchName(value)
        if len(a)==0:
            return abort(404)
        return render_template("result2.html", Book_list= a)

@app.route("/category/search/<value>", methods= ["GET"])
def categorySearch(value):
    try:
        a= employee.searchCategoryID(int(value))
        return jsonify("Category",a)
    except Exception:
        value= value.replace("-"," ")
        a= employee.searchCategoryName(value)
        if len(a)==0:
            abort(404)
        return jsonify("Category",a)

@app.route("/shoppingcart", methods= ["GET"])
def showCart():
    return jsonify(shopping_cart)

@app.route("/shoppingcart/sell", methods= ["PUT"])
def sell_book_from_cart():
    seller1= seller("kyle",24,"male")
    if len(shopping_cart)>0:
        result= seller1.sell_book_from_cart(shopping_cart)
        return jsonify("Bills",result)
    else:
        return "The shopping cart is empty"


@app.route("/book/<userinput>/delete", methods=["DELETE"])
def delete_book(userinput):
    try:
        book_id= int(userinput)
        try:
            a= employee.searchID(book_id)
            book.delBookHelper(book_id)
            return jsonify("Delete Book",a)
        except TypeError:
            return "Cannot find the book"
    except Exception:
        return 'Bad request'
            
    
if __name__=="__main__":
    shopping_cart={}
    bills={}
    app.run(debug=True)




# Sqlite.createDataBase()
# A= category("pokemon adventure",2)
# B= category("test Pokemon", 1)
# Book1= book("pokemon",(1,2),12,12,8)
# book.addBookHelper(Book1)
# category.addCategoryHelper(A)
# category.addCategoryHelper(B)
# conn= sqlite3.connect("BookStore.db")
# with conn:
#     c= conn.cursor()
#     c.execute("Select * from BookCategory")
#     print(c.fetchall())