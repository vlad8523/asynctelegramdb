from .base import BaseModel
from sqlalchemy import Column, BigInteger, Text


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger, unique=True, nullable=False, primary_key=True)
    name = Column(Text, unique=False, nullable=True)

    def __str__(self) -> str:
        return f'<User:({self.user_id})>'

    def __repr__(self):
        return self.__str__()
