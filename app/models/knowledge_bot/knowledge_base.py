from sqlalchemy import Column, BigInteger, String, Text, Boolean, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func
from app.core.database import Base


class KnowledgeBase(Base):
    __tablename__ = "knowledge_base"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    title = Column(String(255), nullable=False)
    file_type_id = Column(BigInteger, ForeignKey("mst_file_type.id"), nullable=False)
    file_path = Column(Text)
    url_path = Column(Text)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)



# Master Tables

class MST_FileType(Base):
    __tablename__ = "mst_file_type"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=True)