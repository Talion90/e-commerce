import os

from fastapi import Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient

from models.goods import Good, UpGood

client = AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.college

router = APIRouter(prefix="routers")


@router.get('/categories')
def categories_of_goods():
    pass


@router.get('/all')
def list_of_goods():
    pass


@router.get('/{id}')
def retrieve_good(id: str):
    pass


@router.post("/", response_description="Add new good", response_model=Good)
async def create_good(good: Good = Body(...)):
    good = jsonable_encoder(good)
    new_good = await db["goods"].insert_one(good)
    created_good = await db["goods"].find_one({"_id": new_good.inserted_id})
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content=created_good)


@router.put("/{id}", response_description="Update a good", response_model=Good)
async def update_good(id: str, good: UpGood = Body(...)):
    good = {k: v for k, v in good.dict().items() if v is not None}

    if len(good) >= 1:
        update_result = await db["goods"].update_one(
            {"_id": id}, {"$set": good})

        if update_result.modified_count == 1:
            if (
                updated_good := await db["goods"].find_one({"_id": id})
            ) is not None:
                return updated_good

    if (existing_good := await db["goods"].find_one({"_id": id})) is not None:
        return existing_good

    raise HTTPException(status_code=404, detail=f"Good {id} not found")


@router.delete("/{id}", response_description="Delete a good")
async def delete_good(id: str):
    delete_result = await db["goods"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(
            status_code=status.HTTP_204_NO_CONTENT,
            content="Good removed successfully",
        )

    raise HTTPException(status_code=404, detail=f"Good {id} not found")
