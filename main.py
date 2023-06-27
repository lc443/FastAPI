from typing import List
from uuid import UUID,  uuid4
from fastapi import HTTPException, FastAPI
from models import Gender, Role, User, UserUpdateRequest

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

# GET ALL
@app.get("/api/v1/users")
async def get_users():
    return hardcoded_db

# POST ONE
@app.post("/api/v1/users")
async def register_user(user: User):
    user.id = uuid4()
    hardcoded_db.append(user)
    return user

# DELETE ONE
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
   for user in hardcoded_db:
       if user.id == user_id:
           hardcoded_db.remove(user)
           return
   raise HTTPException(
       status_code=404,
       detail=f"user with id: {user_id} does not exists"
    )

# Update one
@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID): 
    for user in hardcoded_db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.gender is not None:
                user.gender = user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
        return user
    raise HTTPException(
        status_code=404,
         detail=f"user with id: {user_id} does not exists"
    )


