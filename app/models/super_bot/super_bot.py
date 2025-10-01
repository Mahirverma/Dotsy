from sqlalchemy import Column, BigInteger, String, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from app.core.database import Base


class SuperBot(Base):
    __tablename__ = "super_bot"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    name = Column(String(255), nullable=False)
    intention = Column(Text, nullable=False)

    user_name = Column(String(255), nullable=False)
    mobile = Column(String(20), nullable=False)
    email = Column(String(255), nullable=False)

    prefix_prompt = Column(Text, nullable=False)
    suffix_prompt = Column(Text, nullable=False)
    welcome_message = Column(Text, nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)