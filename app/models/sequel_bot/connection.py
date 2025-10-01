from sqlalchemy import Column, BigInteger, String, Text, Boolean, Integer, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from app.core.database import Base


class Connection(Base):
    __tablename__ = "connection"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    bot_id = Column(BigInteger, ForeignKey("sequel_bot.id", ondelete="CASCADE"), nullable=False)

    connection_type_id = Column(BigInteger, ForeignKey("mst_connection_type.id", ondelete="RESTRICT"), nullable=False)
    host = Column(String(255), nullable=False)
    port = Column(Integer, nullable=False)

    username = Column(String(255), nullable=False)
    password = Column(Text, nullable=False)

    schema_name = Column(String(255), nullable=True)

    is_active = Column(Boolean, default=True, nullable=False)
    ssl_mode_id = Column(BigInteger, ForeignKey("mst_ssl_mode.id"), nullable=False)
    character_set_id = Column(BigInteger, ForeignKey("mst_character_set.id"), nullable=False)
    authentication_method_id = Column(BigInteger, ForeignKey("mst_auth_method.id"), nullable=False)

    connection_pool = Column(Integer, nullable=True)
    idle_timeout = Column(Integer, nullable=True)
    schema_search_path = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


# Master Tables

class MST_ConnectionType(Base):
    __tablename__ = "mst_connection_type"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)   # e.g., PostgreSQL, MySQL, SQLite, MSSQL
    description = Column(String(255), nullable=True) 

class MST_SSLMode(Base):
    __tablename__ = "mst_ssl_mode"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)  # disable, require, verify-ca, verify-full
    description = Column(String(255), nullable=True)

class MST_CharacterSet(Base):
    __tablename__ = "mst_character_set"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

class MST_AuthMethod(Base):
    __tablename__ = "mst_auth_method"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)