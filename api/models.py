from datetime import time
from sqlalchemy import Column, Integer, String, DateTime, sql
from sqlalchemy.orm import relationship

from database import Base


class TestRequest(Base):
    __tablename__ = "ml_request"

    id = Column(Integer, primary_key=True, index=True)
    input = Column(String, default='None')
    created_at = Column(
        DateTime(timezone=True),
        server_default=sql.func.now(), autoincrement=True
    )
