import uuid

from fastapi import FastAPI

from models.course import Course, CourseRequests, CourseResponse
from models.player import Player, PlayerRequests, PlayerResponse


app = FastAPI()

players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}

## Players
@app.get("/players")
async def get_players() -> list[Player]:
    return players.values()

@app.post("/players")
async def create_player(player: PlayerRequests) -> PlayerResponse:
    player_id = uuid.uuid4()
    players[player_id] = Player(id=player_id, name=player.name, handicap=player.handicap)
    return PlayerResponse(id=player_id)

@app.put("/players/{player_id}")
async def update_player(player_id: uuid.UUID, updated_player: PlayerRequests) -> PlayerResponse:
    players[player_id] = Player(id=player_id, name=updated_player.name, handicap=updated_player.handicap)
    return PlayerResponse(id=player_id)

@app.delete("/players/{player_id}")
async def delete_player(player_id: uuid.UUID) -> None:
    players.pop(player_id)

## Courses
@app.get("/courses")
async def courses_list() -> list[Course]:
    return courses.values()

@app.post("/courses")
async def create_course(new_course_request: CourseRequests ) -> CourseResponse:
    course_id = uuid.uuid4()
    courses[course_id] = Course(
        id=course_id, 
        name=new_course_request.name, 
        location=new_course_request.location, 
        holes=new_course_request.holes
        )
    return CourseResponse(id=course_id)

@app.put("/courses/{course_id}")
async def update_course(course_id: uuid.UUID, updated_course: CourseRequests) -> CourseResponse:
    courses[course_id] = Course(
        id=course_id, 
        name=updated_course.name, 
        location=updated_course.location, 
        holes=updated_course.holes
        )
    return CourseResponse(id=course_id)

@app.delete("/courses/{course_id}")
async def delete_course(course_id: uuid.UUID) -> None:
    courses.pop(course_id)