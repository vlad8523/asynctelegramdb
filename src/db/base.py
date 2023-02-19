from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, DeclarativeMeta

BaseModel: DeclarativeBase = declarative_base()
