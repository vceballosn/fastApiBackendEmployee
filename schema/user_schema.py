from pydantic import BaseModel, Field
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[int] = None
    firstName: str  # <--- Snake case
    lastName: str   # <--- Snake case
    email: str    # <--- Snake case