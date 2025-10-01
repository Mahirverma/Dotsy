from sqlalchemy import Column, BigInteger, String, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from app.core.database import Base


class SchemaDefinition(Base):
    __tablename__ = "schema_definition"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    bot_id = Column(BigInteger, ForeignKey("sequel_bot.id", ondelete="CASCADE"), nullable=False)
    object_name = Column(String(255), nullable=False)
    object_type_id = Column(BigInteger, ForeignKey("mst_object_type.id", ondelete="RESTRICT"), nullable=False)
    keyword = Column(String(255), nullable=True)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


# Master Table

class MST_ObjectType(Base):
    __tablename__ = "mst_object_type"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)  # table, view, function, procedure
    description = Column(Text, nullable=True)