"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):

    db.app = app
    db.init_app(app)


class User(db.Model):
    '''User class.'''

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(),
                           nullable=False)
    last_name = db.Column(db.String(),
                          nullable=False)
    img_URL = db.Column(db.String(),
                        nullable=True,
                        default='https://picsum.photos/100')

    # def combine_name(self):
    #     return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        """Show info about user."""

        u = self
        return f"<User {u.id} {u.first_name} {u.last_name} {u.img_URL}>"


class Post(db.Model):
    '''Post class.'''

    __tablename__ = 'posts'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(100),
                      nullable=False)
    content = db.Column(db.String(3000),
                      nullable=False)
    created_at = db.Column(db.DateTime,
                           default=datetime.utcnow)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'))

    user = db.relationship('User',
                           backref='posts')

    def __repr__(self):
        """Show info about user."""

        p = self
        return f"<Post {p.id} {p.title} {p.content} {p.created_at} {p.user_id}>"


class Tag(db.Model):
    '''Tag class.'''
    __tablename__ = 'tags'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String, unique=True)

    posts = db.relationship('Post',
                        secondary='post_tags',
                           backref='tags')

    def __repr__(self):
        """Show info about user."""
        t = self
        return f"<Tag {t.id} {t.name}>"


class PostTag(db.Model):
    '''PostTag class.'''
    __tablename__ = 'post_tags'

    post_id = db.Column(db.Integer,
                        db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer,
                        db.ForeignKey('tags.id'), primary_key=True)


    def __repr__(self):
        """Show info about user."""

        pt = self
        return f"<PostTag {pt.post_id} {pt.tag_id}>"

