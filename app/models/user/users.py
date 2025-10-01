from sqlalchemy import Column, String, Integer, Boolean, DateTime, BigInteger, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    company_id = Column(
        BigInteger,
        ForeignKey("company.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )   
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)  # can be auto-generated in code
    full_name = Column(String(255))
    token = Column(String(50))
    token_expiry = Column(DateTime(timezone=True))  # set in code: now() + 15 minutes
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )