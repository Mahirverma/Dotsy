from sqlalchemy import Column, BigInteger, String, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from app.core.database import Base


class ExcelFile(Base):
    __tablename__ = "excel_file"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    bot_id = Column(BigInteger, ForeignKey("excel_bot.id", ondelete="CASCADE"), nullable=False)

    file_name = Column(String(255), nullable=False)
    file_path = Column(Text, nullable=False)

    uploaded_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)