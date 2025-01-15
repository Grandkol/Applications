from uuid import UUID
from datetime import datetime

from typing_extensions import Optional
from pydantic import BaseModel

class ApplicationToBD(BaseModel):
    user_name: Optional[str] = None
    description: Optional[str] = None

class ApplicationInBd(BaseModel):
    id: UUID
    user_name: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[datetime] = None