from pydantic import BaseModel, Field
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[int] = None
    first_name: str  # <--- Snake case
    last_name: str   # <--- Snake case
    email_id: str    # <--- Snake case