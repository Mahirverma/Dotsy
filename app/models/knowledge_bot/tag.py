from sqlalchemy import Column, BigInteger, ForeignKey, String
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from app.core.database import Base

class Tag(Base):
    __tablename__ = "tag"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    knowledge_base_id = Column(BigInteger, ForeignKey("knowledge_base.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(100), nullable=False, unique=True)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)