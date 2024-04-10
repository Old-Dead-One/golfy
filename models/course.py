from uuid import UUID

from pydantic import BaseModel


class Course(BaseModel):
    id: UUID
    name: str
    location: str
    holes: int


class Course(BaseModel):
    id: UUID
    name: str
    location: str

class CourseRequests(BaseModel):
    name: str
    location: float
    holes: int

class CourseResponse(BaseModel):
    id: UUID