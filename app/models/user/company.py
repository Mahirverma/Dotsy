from sqlalchemy import Column, String, Integer, Boolean, DateTime, BigInteger, Text, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Company(Base):
    __tablename__ = "company"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    contact_email = Column(String(255), nullable=False)
    mobile = Column(Integer, nullable=False)
    address = Column(String(255), nullable=False)
    industry_type_id = Column(BigInteger,ForeignKey("mst_industry_type.id", ondelete="RESTRICT"), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

# Master Tables

class MST_IndustryType(Base):
    __tablename__ = "mst_industry_type"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
