from sqlalchemy import Column, Integer, String

from app.rag.services.database import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    original_filename = Column(String, nullable=False)
    stored_filename = Column(String, nullable=False)
    file_hash = Column(String, unique=True, nullable=False)
    chunks_created = Column(Integer, default=0)
