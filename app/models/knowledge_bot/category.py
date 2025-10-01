from sqlalchemy import Column, BigInteger, String, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from app.core.database import Base

class MST_Category(Base):
    __tablename__ = "mst_category"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class KnowledgeBaseCategory(Base):
    __tablename__ = "knowledge_base_category"

    knowledge_base_id = Column(BigInteger, ForeignKey("knowledge_base.id", ondelete="CASCADE"), primary_key=True)
    category_id = Column(BigInteger, ForeignKey("mst_category.id", ondelete="CASCADE"), primary_key=True)

    __table_args__ = (
        UniqueConstraint("knowledge_base_id", "category_id", name="uq_knowledge_base_category"),
    )

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)