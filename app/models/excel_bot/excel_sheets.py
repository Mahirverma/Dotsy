from sqlalchemy import Column, BigInteger, String, Text, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from app.core.database import Base


class ExcelSheet(Base):
    __tablename__ = "excel_sheet"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    file_id = Column(BigInteger, ForeignKey("excel_file.id", ondelete="CASCADE"), nullable=False)

    sheet_name = Column(String(255), nullable=False)
    sheet_path = Column(Text, nullable=False)  # optional: can store path in storage if needed

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)

class BotSheetSelection(Base):
    __tablename__ = "bot_sheet_selection"

    bot_id = Column(BigInteger, ForeignKey("excel_bot.id", ondelete="CASCADE"), primary_key=True)
    sheet_id = Column(BigInteger, ForeignKey("excel_sheet.id", ondelete="CASCADE"), primary_key=True)

    __table_args__ = (
        UniqueConstraint("bot_id", "sheet_id", name="uq_bot_sheet_selection"),
    )

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)