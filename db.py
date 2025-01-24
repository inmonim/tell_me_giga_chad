from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

from model import Log

_env = dotenv_values('.env')

_host = _env.get('DB_HOST')
_username = _env.get('DB_USERNAME')
_password = _env.get("DB_PASSWORD")
_table = _env.get("DB_TABLE")

_engine = create_engine(f"mysql+pymysql://{_username}:{_password}@{_host}:3306/{_table}",
                        pool_recycle=3600)

session = sessionmaker(bind=_engine)

with session() as db:
    db.add(Log(answer="test", question="test", token=1))
    db.commit()