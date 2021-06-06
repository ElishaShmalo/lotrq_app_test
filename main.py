from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import *
from sqlalchemy import func
import uvicorn

app = FastAPI(debug=True)
templates = Jinja2Templates("/templates")

Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
def home(req:Request):
    return templates.TemplateResponse("home.html", {"request": req})

@app.get("/get/chardata", response_class=RedirectResponse)
async def clicked_button(name:str):
    db:Session = SessionLocal()

    fullname = db.query(CharacterInfoTable).filter(func.lower(CharacterInfoTable.name) == func.lower(name)).first().fullname

    db.close()
    return RedirectResponse(f"/show?fullname={fullname}")

@app.get("/show", response_class=HTMLResponse)
def show(req:Request, fullname:str):
    return templates.TemplateResponse("show.html", {"request": req, "char_name": fullname})

@app.post("/make/qoute")
def quote(data:CharacterQuote):
    db = SessionLocal()
    
    new_qoute = CharacterQuotesTable(name=data.name, details=data.details, quote=data.quote)
    db.add(new_qoute)
    db.commit()
    db.refresh(new_qoute)

    db.close()

    return new_qoute

@app.post("/make/img")
def img(data:CharacterImge):
    db:Session = SessionLocal()

    new_img = CharacterImgTable(name=data.name, img=data.img)
    db.add(new_img)
    db.commit()
    db.refresh(new_img)

    db.close()

    return img

@app.post("/make/char")
def char(data:CharacterInfo):
    db:Session = SessionLocal()

    new_char = CharacterInfoTable(name=data.name, fullname=data.fullname, aka=data.aka)

    db.add(new_char)
    db.commit()
    db.refresh(new_char)
    db.close()

    return data

