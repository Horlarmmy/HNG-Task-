from fastapi import FastAPI, HTTPException
import datetime
# Instantiate the class
app = FastAPI(
    title="HNGX",
    description="Backend Task 2",
)

@app.get("/")
def hello():
    return {"message":"Welcome!!!"}


@app.post("/api")
def details(slack_name: str, track: str):
    return {"id": 1, "name": "Alade Toheeb"}

@app.get("/api/{id}")
def getUser():
    return {"id": 1, "name": "Alade Toheeb"}

@app.delete("/api/{id}")
def delUser():
    pass

@app.put("/api/{id}")
def updateUser():
    return {"id": 1, "name": "Alade Toheeb"}