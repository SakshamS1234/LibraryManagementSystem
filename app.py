from flask import Flask,render_template,request,redirect
from models import db, LibraryBookList, LibraryMemberList
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/data/createbook' , methods = ['GET','POST'])
def createbook():
    if request.method == 'GET':
        return render_template('createbook.html')
 
    if request.method == 'POST':
        bookID = request.form['bookID']
        bookTitle = request.form['bookTitle']
        bookAuthor = request.form['bookAuthor']
        bookCopies = request.form['bookCopies']
        book = LibraryBookList(bookID = bookID, bookTitle = bookTitle, 
                               bookAuthor = bookAuthor, bookCopies = bookCopies)
        db.session.add(book)
        db.session.commit()
        return redirect('/data')


@app.route('/data/createmember', methods = ['GET','POST'])
def createmember():    
    if request.method == 'POST':
        memberID = request.form['memberID']
        memberName = request.form['memberName]
        memberRegDate = request.form['memberRegDate']
        memberBookTaken = request.form['memberBookTaken']
        member = LibraryBookList(memberID = memberID, memberName = memberName,
                                 memberRegDate = memberRegDate,
                                 memberBookTaken = memberBookTaken)
        db.session.add(member)
        db.session.commit()
        return redirect('/data')
    return render_template('createmember.html')


@app.route('/data')
def retrievelist():
    books = LibraryBookList.query.all()
    members = LibraryMemberList.query.all()
    return render_template('datalist.html', books = books,
                           members = members)

 
@app.route('/data/books/<int:id>')
def retrievebooks(id):
    book = LibraryBookList.query.filter_by(bookID=id).first()
    if book:
        return render_template('booksdata.html', LibraryBookList = LibraryBookList)
    return f"There is no such book."


@app.route('/data/members/<int:id>')
def retrievemembers(id):
    member = LibraryMemberList.query.filter_by(memberID=id).first()
    if member:
        return render_template('membersdata.html', LibraryMembersList = LibraryMembersList)
    return f"There is no such member."    

 
@app.route('/data/books/<int:id>/update',methods = ['GET','POST'])
def bookupdate(id):
    book = LibraryBookList.query.filter_by(bookID=id).first()
    if request.method == 'POST':
        if book:
            db.session.delete(book)
            db.session.commit()
            bookTitle = request.form['bookTitle']
            bookAuthor = request.form['bookAuthor']
            bookCopies = request.form['bookCopies']
            book = LibraryBookList(bookID = id, bookTitle = bookTitle,
                                     bookAuthor = bookAuthor, bookCopies = bookCopies)
            db.session.add(book)
            db.session.commit()
            return redirect(f'/data/books/{id}')
        return f"There is no such book."
 
    return render_template('booksupdate.html', LibraryBookList = LibraryBookList)

    
@app.route('/data/members/<int:id>/update',methods = ['GET','POST'])
def memberupdate(id):
    member = LibraryMembersList.query.filter_by(memberID=id).first()
    if request.method == 'POST':
        if book:
            db.session.delete(member)
            db.session.commit()
            memberName = request.form['memberName']
            memberRegDate = request.form['memberRegDate']
            memberBookTaken = request.form['memberBookTaken']
            member = LibraryMembersList(memberID = id, memberName = memberName,
                                        memberRegDate = memberRegDate,
                                        memberBookTaken = memberBookTaken)
            db.session.add(member)
            db.session.commit()
            return redirect(f'/data/member/{id}')
        return f"There is no such member."
 
    return render_template('membersupdate.html', LibraryMembersList = LibraryMembersList)
 
    
@app.route('/data/book/<int:id>/delete', methods=['GET','POST'])
def booksdelete(id):
    book = LibraryBookList.query.filter_by(bookID=id).first()
    if request.method == 'POST':
        if book:
            db.session.delete(book)
            db.session.commit()
            return redirect('/booksdata')
        abort(404)
 
    return render_template('booksdelete.html')
 
    
 @app.route('/data/book/<int:id>/delete', methods=['GET','POST'])
 def membersdelete(id):
     member = LibraryMembersList.query.filter_by(memberID=id).first()
     if request.method == 'POST':
         if member:
             db.session.delete(member)
             db.session.commit()
             return redirect('/membersdata')
         abort(404)
  
     return render_template('membersdelete.html')
    
 
app.run(host='localhost', port=5000)