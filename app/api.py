from fastapi import FastAPI

router = FastAPI()

entries = []
users = []

@router.get("/")
def welcome():
    return {
        "message": "Welcome to the FastAPI + Okteto series in development mode!"
    }

@router.get("/entries")
def retrieve_entries():
    return {
        "entries": entries
    }

@router.post("/entry")
def add_entry(data: dict):
    entries.append(data)
    return {
        "message": "Entry added successfully with id {}!".format(len(entries))
    }

@router.delete("/entry/id")
def delete_entry(id: int):
    entries.pop(id)
    return {
        "message": "Entry deleted successfully"
    }

@router.post("/user/new")
def register_user(data: dict):
    users.append(data)
    return {
        "message": "User registration successful"
    }

@router.post("/user")
def login_user(user: dict):
    if user in users:
        return {
            "message": "User logged in successfully!"
        }
    return {
        "message": "Invalid details!"
    }