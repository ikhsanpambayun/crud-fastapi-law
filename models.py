from sqlalchemy import Column, String, Integer

from database import Base


class Guitar(Base):
    __tablename__ = "guitars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    description = Column(String)