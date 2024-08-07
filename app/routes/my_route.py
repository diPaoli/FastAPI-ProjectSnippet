from fastapi import Response, APIRouter, status, Depends
from fastapi.responses import JSONResponse

from app.schemas.my_schema import MySchema
from app.utils.token import validate_token


router = APIRouter(dependencies=[Depends(validate_token)])


@router.get("/{id}")
def get_(id: int):
    return JSONResponse({"id": id}, status_code=status.HTTP_200_OK)


@router.post("/")
def post_(data: dict = None):
    schema = MySchema()

    if data:
        schema = MySchema(**data)

    return JSONResponse(schema.model_dump(), status_code=status.HTTP_201_CREATED)
