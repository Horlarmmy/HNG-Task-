from fastapi import FastAPI, HTTPException
import datetime
# Instantiate the class
app = FastAPI(
    title="HNGX",
    description="Backend Task 1",
)

@app.get("/")
def hello():
    return {"message":"Welcome!!!"}


@app.post("/api")
def details(slack_name: str, track: str):
    return {
        "slack_name": slack_name,
        "current_day": datetime.datetime.now().strftime('%A'),
        "utc_time": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": "https://github.com/Horlarmmy/HNG-Tasks/blob/main/task1/main.py",
        "github_repo_url": "https://github.com/Horlarmmy/HNG-Tasks/blob/main/task1/",
        "status_code": 200
        }
