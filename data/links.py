import sqlalchemy
from .db_session import SqlAlchemyBase


class Link(SqlAlchemyBase):
    __tablename__ = 'links'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    short = sqlalchemy.Column(sqlalchemy.String)
    full = sqlalchemy.Column(sqlalchemy.String)
