from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class LibraryBookList(db.Model):
    __tablename__ = "LibraryBookList"
 
    bookID = db.Column(db.Integer, primary_key = True)
    bookTitle = db.Column(db.String())
    bookAuthor = db.Column(db.String())
    bookCopies = db.Column(db.Integer())
 
    def __init__(self, bookID, bookTitle, bookAuthor, bookCopies):
        self.bookID = bookID
        self.bookTitle = bookTitle
        self.bookAuthor = bookAuthor
        self.bookCopies = bookCopies
 
    def __repr__(self):
        return f"{self.bookTitle} by {self.bookAuthor}"
    
class LibraryMembersList(db.Model):
    __tablename__ = "LibraryMembersList"
    
    memberID = db.Column(db.Integer, primary_key = True)
    memberName = db.Column(db.String())
    memberRegDate = db.Column(db.Date())
    memberBookTaken = db.Column(db.Integer, ForeignKey('LibraryBookList.bookID'))
    
    def __init__(self, memberID, memberName, memberRegDate, memberBookTaken):
        self.memberID = memberID
        self.memberName = memberName
        self.memberRegDate = memberRegDate
        self.memberBookTaken = memberBookTaken
        
    def __repr__(self):
        return f"ID: {self.memberID}\nName: {self.memberName}\nBook Taken: {self.memberBookTaken}"