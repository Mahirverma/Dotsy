from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base

class DocumentContent(Base):
    __tablename__ = "document_contents"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id", ondelete="CASCADE"))
    chunk_index = Column(Integer, nullable=False)  # order of chunks
    content = Column(Text, nullable=False)  # actual text content
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    document = relationship("Document", backref="contents")
