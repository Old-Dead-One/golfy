import uuid

from fastapi import FastAPI

from models.player import Player, CreatePlayerRequest
from models.course import Course


app = FastAPI()

players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}


# Players
@app.get("/players")
async def list_players() -> list[Player]:
    return players.values()

@app.post ("/players")
async def create_player(player_detail: CreatePlayerRequest) -> uuid.UUID:
    player_id = uuid.uuid4()
    player = Player(id=player_id, name=player_detail.name, handicap=player_detail.handicap)
    players[player_id] = player
    return player.id

#
#@app.put ("/players/{player_id}")
#async def update_player():
#    pass
#
#@app.delete ("/players/{player_id}")
#async def remove_player ():
#    pass
#
## Courses
#@app.get("/courses")
#async def course_list() -> list[Course]:
#    return players.values
#
#@app.post ("/courses")
#async def add_course(courses: Course) -> uuid.UUID:
#    courses[]
#
#@app.put ("/courses/{course_id}")
#async def update_course():
#    pass
#
#@app.delete ("/courses/{course_id}")
#async def remove_course():
#    pass