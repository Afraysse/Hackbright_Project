""" 
OpenBook 2.0 uses SQLAlchemy and PostgreSQL to store and query user and 
site information. 

"""

from flask_sqlalchemy import SQLAlchemy

import datetime

# search engines uses the library SQLAlchemy-searchable 

from sqlalchemy_searchable import make_searchable
from sqlalchemy_utils.types import TSVectorType  

db = SQLAlchemy()

make_searchable()

############################################################
# db tables for Model.py

class User(db.Model):
    """ Contains user information. """

    __tablename__ = "user"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    # created_at = db.Column()

    def __repr__(self):

        return "<User user_id={} email={}>".format(self.user_id, self.email)

class OwnedThreads(db.Model):
    """ Contains owned thread information per user. """

    __tablename__ = "owned_threads"

    owned_thread_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    public_or_private = db.Column(db.String, nullable=False)
    live_or_closed = db.Column(db.String, nullable=False)

    def __repr__(self):

        return "<OwnedThreads owned_thread_id={} public_or_private={} live_or_closed={}>".format(self.owned_thread_id, 
                                                                                        self.public_or_private, self.live_or_closed)

class ParticipantThreads(db.Model):
    """ Contains active participant threads according to user. """

    __tablename__ = "participant_threads"

    participant_thread_id = db.Column(db.String(600))

################################################################################

def connect_to_db(app):
    """ Connect to the database in Flask app. """

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///threaded'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."


