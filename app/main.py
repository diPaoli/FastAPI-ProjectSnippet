from decouple import config
from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response

from app.routes.health import router as health_router
from app.config.database import Base, engine


app = FastAPI()
router = APIRouter()

app.include_router(router)
app.include_router(health_router)


@router.get('/')
def get():
    return {"message": "OK"}


@router.post('/{topic}')
def post(topic: str):
    return {"message": f"OK - {topic}"}


Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=config('ALLOWED_ORIGINS'),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# pylint: disable=broad-except
@app.middleware("http")
async def run_request(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as err:
        if response and hasattr(response.content):
            return Response(response.content, status_code=response.status_code)

        return JSONResponse(content={"message": str(err)}, status_code=500)
