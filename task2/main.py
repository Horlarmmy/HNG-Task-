from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from db import Base, engine, SessionLocal
from pydantic import BaseModel
import models


# Instantiate the class
app = FastAPI(
    title="HNGX",
    description="Backend Task 2",
)


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Person(BaseModel):
    name: str

@app.get("/")
def hello():
    return {"message":"Welcome!!!"}


@app.post("/api")
def createUser(person: Person, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.name == person.name).first():
        raise HTTPException(status_code=400, detail="User with the name already exists")
    # create the user
    user = models.User(name=person.name)
    print(user.name)

    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "name": user.name}

@app.get("/api/{id}")
def getUser(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if (user):
        return {"id": user.id, "name": user.name}
    else:
        raise HTTPException(status_code=400, detail="User with id {} doesn't exists".format(id))

@app.delete("/api/{id}", status_code=204)
def delUser(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if (user):
        db.delete(user)
        db.commit()
    else:
        raise HTTPException(status_code=400, detail="User with id {} doesn't exists".format(id))

@app.put("/api/{id}")
def updateUser(person: Person, id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if (user):
        if db.query(models.User).filter(models.User.name == person.name).first():
            raise HTTPException(status_code=400, detail="User with the name already exists")
        setattr(user, 'name', person.name)
        db.commit()
        return {"id": user.id, "name": user.name}
    else:
        raise HTTPException(status_code=400, detail="User with id {} doesn't exists".format(id))

