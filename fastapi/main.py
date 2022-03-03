from typing import Optional, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import randint

users = {
    "142": {
        "id": "142",
        "firstName": "Alice",
        "lastName": "Smith",
        "email": "alice.smith@gmail.com",
        "dateOfBirth": "1997-10-31",
        "emailVerified": True,
        "signUpDate": "2019-08-24"
    }
}

app = FastAPI(
    debug=True,
    title="Test"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/user")
def get_user():
    return [user for user in users.values()]

@app.get("/user/{user_id}")
def get_user_by_id(user_id: str):
    return users.get(user_id, [])

@app.post("/user")
def update_user(user: Dict):
    user_id = str(randint(0, 1000000))
    users[user_id] = {
        **user,
        "id": user_id,
        "emailVerified": True,
        "signUpDate": "2019-08-24"
    }
    print(users)

    return users[user_id]
