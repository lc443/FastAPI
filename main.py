from typing import List
from uuid import uuid4
from click import UUID
from fastapi import FastAPI
from models import Gender, Role, User

app = FastAPI()


hardcoded_db: List[User] = [
    User(
        id=UUID("b496140f-fec0-40d1-9c4e-f2a7e8ad41a9"),
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),

        User(
        id=UUID("eb3c829a-3bd4-4ccf-a670-169ef5f6d4fa"),
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),

    User(
        id=uuid4(),
        first_name="Collin",
        last_name="Robinson",
        gender=Gender.male,
        roles=[Role.admin, Role.user, Role.student]
    )

]
    
@app.get("/")
async def root():
    return  {"Hello": "World"}

@app.get("/api/v1/users")
async def get_users():
    return hardcoded_db

@app.post("/api/v1/users")
async def register_user(user: User):
    user.id = uuid4()
    hardcoded_db.append(user)
    return user
