from sqlalchemy import (Column, Integer, String, BigInteger,
                        Boolean, ForeignKey, DateTime)
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    user_city = Column(String, nullable=True)
    birthday = Column(String, nullable=True)
    reg_date = Column(DateTime, default=datetime.now())


class Hashtag(Base):
    __tablename__ = "hashtag"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    hashtag = Column(String, nullable=False)


class UserPost(Base):
    __tablename__ = "userposts"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    hashtag = Column(String, ForeignKey("hashtag.hashtag"))
    main_text = Column(String)
    reg_date = Column(DateTime, default=datetime.now())

    user_fk = relationship(User, lazy="subquery")
    hashtag_fk = relationship(Hashtag, lazy="subquery")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    post_id = Column(BigInteger, ForeignKey("userposts.id"))
    text = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())

    user_fk = relationship(User, lazy="subquery")
    post_fk = relationship(UserPost, lazy="subquery")


class PostPhoto(Base):
    __tablename__ = "photo"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    photo_path = Column(String, nullable=False)
    post_id = Column(BigInteger, ForeignKey("userposts.id"))
    reg_date = Column(DateTime, default=datetime.now())

    post_fk = relationship(UserPost, lazy="subquery")
