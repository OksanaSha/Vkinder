import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import date

Base = declarative_base()
engine = sq.create_engine('postgresql://oks:@localhost:5432/vk_users_db', client_encoding='utf8')
Session = sessionmaker(bind=engine)

class FoundUsers(Base):
    __tablename__ = 'found_users'

    vk_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, nullable=False)
    url = sq.Column(sq.String, unique=True, nullable=False)
    photos = sq.Column(sq.String, nullable=False)
    bot_user = relationship('BotStart', secondary='bot_users_to_found_users')


bot_users_to_found_users = sq.Table(
    'bot_users_to_found_users', Base.metadata,
    sq.Column(sq.Integer, sq.ForeignKey('bot_users.user_id')),
    sq.Column(sq.Integer, sq.ForeignKey('found_users.vk_id'))
)

class BotUsers(Base):
    __tablename__ = 'bot_users'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, nullable=False)
    date_find = sq.Column(sq.Date, default=date.today)
    found_user = relationship(FoundUsers, secondary='bot_users_to_found_users')

