"""Database program"""
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

Base = declarative_base()


class Country(Base):
    """Country class"""
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    leagues = relationship("League", back_populates="country")


class League(Base):
    """League class"""
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey("countries.id"))

    country = relationship("Country", back_populates="leagues")
    teams = relationship("Team", back_populates="league")


class Team(Base):
    """Team class"""
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    league_id = Column(Integer, ForeignKey("leagues.id"))

    league = relationship("League", back_populates="teams")
    players = relationship("Player", back_populates="team")


class Player(Base):
    """Player class"""
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))

    team = relationship("Team", back_populates="players")


class Match(Base):
    """Match class"""
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    home_team_id = Column(Integer, ForeignKey("teams.id"))
    away_team_id = Column(Integer, ForeignKey("teams.id"))
    date = Column(Date)
    score = Column(String)


DATABASE_URL = "postgresql://postgres:1@localhost/football_db"

engine = create_engine(DATABASE_URL)
SESSION_LOCAL = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    """Get db fuction"""
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()
