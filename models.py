from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    """
CREATE TABLE users(
  user_id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT UNIQUE,
  created_at INTEGER NOT NULL,
  town_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES meetups (meetup_id)
);
"""
    __tablename__ = 'users'
    user_id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    name = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))

    # meetups_list da użytkownikowi listę obiektów Meetup utworzonych wydarzeń
    # comments_list da użytkownikowi listę obiektów Post utworzonych komentarzy
    meetups_list = relationship("Meetup", back_populates="meetup_creator", cascade="all, delete-orphan")
    comments_list = relationship("Comment", back_populates="commented_event", cascade="all, delete-orphan")


class Meetup(Base):
    """
    CREATE TABLE meetups(
      meetup_id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT UNIQUE,
      created_at INTEGER NOT NULL,
      town_id INTEGER NOT NULL,
      name TEXT NOT NULL,
      FOREIGN KEY (town_id) REFERENCES towns (town_id)
    );
    """

    __tablename__ = 'meetups'

    meetup_id = Column(Integer(), primary_key=True, unique=True)
    user_id = Column(Integer(), ForeignKey('users.user_id'))
    location_id = Column(String(255), ForeignKey('towns.town_id'), nullable=False)
    title = Column(String(100), nullable=False)
    date = Column(String(255), nullable=False)
    description = Column(String(5000), nullable=False)
    status = Column(Boolean(), default=True)
    created_at = Column(Integer())
    activity_people = Column(Boolean())
    activity_animals = Column(Boolean())
    activity_ecology = Column(Boolean())


    # meetup_creator da dostęp do obiektu User użytkownika
    # comments_list da listę obiektów Post przypisanych do meetupu
    meetup_creator = relationship("User", back_populates="meetups_list")
    comments_list = relationship("Comment", back_populates="commented_event", cascade="all, delete-orphan")

    def dict_format(self):
        return {'id': self.id, 'user_responsible': self.meetup_creator.name,
                'title': self.title, 'date': self.date, 'location': self.location,
                'description': self.description, 'status': self.status}


class Post(Base):
    """
CREATE TABLE posts(
  post_id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT UNIQUE,
  user_id INTEGER NOT NULL,
  created_at INTEGER NOT NULL,
  town_id INTEGER NOT NULL,
  metup_id INTEGER NOT NULL,
  message TEXT NOT NULL,
  FOREIGN KEY (post_id) REFERENCES users (user_id)
);
    """

    __tablename__ = 'posts'

    post_id = Column(Integer(), primary_key=True, unique=True)
    user_id = Column(Integer(), ForeignKey('users.user_id'))
    meetup_id = Column(Integer(), ForeignKey('meetups.meetup_id'))
    created_at = Column(String(255))
    message = Column(String(2000), nullable=False)

    # post_author da dostęp do obiektu User użytkownika
    # commented_meetup da listę obiektów Post utworzonych komentarzy przypisanych do meetupu
    post_author = relationship("User", back_populates="comments_list")
    commented_meetup = relationship("Meetup", back_populates="comments_list")


    def dict_format(self):
        return {'id': self.id, 'username': self.post_author.name,
                'date': self.created_at, 'message': self.message}

class Town(Base):
    __tablename__ = 'towns'

    town_id = Column(Integer(), primary_key=True, unique=True)
    name = Column(String(255), nullable=False)
    latlang = Column(String(255), nullable=False, unique=True)

