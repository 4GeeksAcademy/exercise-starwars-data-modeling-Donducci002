import os
import sys
from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

Base = declarative_base()


class Person(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_favorites = relationship("user_Favorites", back_populates="user")
    name = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    nickname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, primary_key=True)
    password = Column(String(250), nullable=False, primary_key=True)



class User_favorites(Base):
    __tablename__ = 'user_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"))
    planet_id = Column(ForeignKey("planet.id"))
    character_id = Column(ForeignKey("character.id"))
    user = relationship("User", back_populates="user_Favorites")
    planet = relationship("Planet", back_populates="user_Favorites")


class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key=True)
    
    user_favorites = relationship("user_Favorites", back_populates="planet")
    name = Column(String(250), nullable=False)
    Climate = Column(String(250), nullable=True)
    Diameter = Column(Integer, nullable=True)
    Gravity = Column(Integer, nullable=True)
    Population = Column(Integer, nullable=True)
    Mass = Column(Integer, nullable=True)


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    
    user_favorites = relationship("user_Favorites", back_populates="character")
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    hairColor = Column(String(250), nullable=True)
    eyeColor = Column(String(250), nullable=True)
    skinColor = Column(String(250), nullable=True)
    gender = Column(String(250), nullable=True)
    birthDate = Column(String(250), nullable=True)
    description = Column(String(250), nullable=True)


# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e