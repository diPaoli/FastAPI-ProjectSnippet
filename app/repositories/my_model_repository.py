from app.config.database import session
from app.models.my_model import MyTable


class MyRepository:
    def get_all_data():
        return session.query(MyTable).all()
