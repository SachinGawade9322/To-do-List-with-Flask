from sqlalchemy import Column, Integer, String, DateTime
from database import Base

# Define SQLAlchemy model for Todo
class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(250))
    time = Column(DateTime)
