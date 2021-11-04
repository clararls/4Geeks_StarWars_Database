import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    user_name = Column(String(30), nullable=False)
    password = Column(String(250), nullable=False)
    favorites_planets = relationship("Favorites_planets")
    favorites_characters = relationship("Favorites_characters")

class Planets(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(30), nullable=False)
    favorites_planets = relationship("Favorites_planets")

class Characters(Base):
    __tablename__='character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(30), nullable=False)
    favorites_characters = relationship("Favorites_characters")

class Favorites_planets(Base):
    __tablename__='favorites_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    planets_id = Column(String, ForeignKey('planets.id'))
    

class Favorites_character(Base):
    __tablename__='favorites_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    character_id = Column(String, ForeignKey('character.id'))
    


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')