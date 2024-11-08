from dotenv import load_dotenv
load_dotenv()

import os
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column ,Integer ,String

SQLALCHEMY_URL = os.getnev("DB_URL")

engine = create_engine()
db_client = sessionmaker(bind=engine)()

BASE = declarative_base()

class table_1(BASE):
    __tablename__ = 'table_1'
    

