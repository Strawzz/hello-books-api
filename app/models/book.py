from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    __tablename__ = "book"

    def to_dict(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "desctiption" : self.description}
        