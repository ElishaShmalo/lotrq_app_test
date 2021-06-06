from lotrq_app.database import Base
from sqlalchemy import Column, String
from pydantic import BaseModel

class CharacterQuotesTable(Base):

    __tablename__ = "character_quotes"

    name = Column(String)
    quote = Column(String, primary_key=True)
    details = Column(String)

class CharacterQuote(BaseModel):
    name:str
    quote:str
    details:str

class CharacterImgTable(Base):

    __tablename__ = "character_imgs"

    name = Column(String)
    img = Column(String, primary_key=True)

class CharacterImge(BaseModel): 
    name:str
    img:str

class CharacterInfoTable(Base):
    __tablename__ = "character_infos"

    name = Column(String, primary_key=True)
    fullname = Column(String)
    aka = Column(String)

class CharacterInfo(BaseModel):

    name:str
    fullname:str
    aka:str
