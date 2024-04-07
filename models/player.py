from uuid import UUID

from pydantic import BaseModel


class Player(BaseModel):
    id: UUID
    name: str
    handicap: float

class PlayerRequests(BaseModel):
    name: str
    handicap: float

class PlayerResponse(BaseModel):
    id: UUID