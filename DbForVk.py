import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

Base = declarative_base()
engine = sq.create_engine('postgresql://:@localhost:5432/vk_users_db', client_encoding='utf8')
Session = sessionmaker(bind=engine)
session = Session()

class FoundUsers(Base):
    __tablename__ = 'users_info'

    vk_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, nullable=False)
    url = sq.Column(sq.String, unique=True, nullable=False)
    photos = sq.Column(sq.String, nullable=False)


class BotUsers(Base):
    __tablename__ = 'bot_users'

    id = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer, nullable=False)
    date_find = sq.Column(sq.Date, default=date.today)