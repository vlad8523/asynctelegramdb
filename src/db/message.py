from .base import BaseModel
from sqlalchemy import Column, BigInteger, Text, ForeignKey


class Message(BaseModel):
    __tablename__ = 'messages'

    message_id = Column(BigInteger, unique=True, nullable=False, primary_key=True)
    text = Column(Text, unique=False, nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.user_id'))

    def __str__(self) -> str:
        return f'<message:({self.message_id}={self.text}) from user:{self.user_id}>'

    def __repr__(self):
        return self.__str__()
