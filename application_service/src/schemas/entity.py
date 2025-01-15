from uuid import UUID
from datetime import datetime

from pydantic import BaseModel

class Application:
    id: UUID
    user_name: str
    description: str
    created_at: datetime
