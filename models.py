"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


default_img = 'https://tinyurl.com/demo-cupcake'


class Cupcake(db.Model):
    """Cupcake"""

    __tablename__ = "cupcakes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    flavor = db.Column(
        db.String(50),
        nullable=False,
    )

    size = db.Column(
        db.String(50),
        nullable=False,
    )

    rating = db.Column(
        db.Integer(),
        nullable=False
    )

    image = db.Column(
        db.String,
        default=default_img,
        nullable=True
    )
    
    def serialize(self):
        "this below will return a dictionary version of a todo this will let you jsonify it later "
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }




def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
