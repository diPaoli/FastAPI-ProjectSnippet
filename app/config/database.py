from datetime import datetime, timezone

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    pass


engine = create_engine(config('PG_URL'))

session = Session(engine)