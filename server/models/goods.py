from bson import ObjectId
from pydantic import BaseModel, Field, NonNegativeFloat, FilePath, FileUrl


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Good(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    price: NonNegativeFloat
    description: str
    category: str
    material: str
    images: FilePath | FileUrl | None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "cashmere",
                "price": 99.99,
                "description": "The best good in the world",
                "category": "tissue",
                "material": "cashmere",
                "images": None,
            }
        }


class UpGood(BaseModel):
    name: str | None
    price: NonNegativeFloat | None
    description: str | None
    category: str | None
    material: str | None
    images: FilePath | FileUrl | None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "cashmere",
                "price": 99.99,
                "description": "The best good in the world",
                "category": "tissue",
                "material": "cashmere",
                "images": None,
            }
        }
