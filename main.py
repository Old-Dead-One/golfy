import uuid

from fastapi import FastAPI

from models.player import Player, PlayerRequests, PlayerResponse
from models.course import Course


app = FastAPI()

players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}


# Players
@app.get("/players")
async def list_players() -> list[Player]:
    return players.values()


@app.post("/players")
async def create_player(player: list_players) -> uuid.UUID:
    player_id = uuid.uuid4()
    players[player_id] = player
    return PlayerResponse(id=player_id)


@app.put("/players/{player_name}")
async def update_player(player: Player) -> Player:
    player = Player(name=player.name, handicap=player.handicap)
    for player in players():
        if player.name == player.name:
            player.handicap = player.handicap
            return player
    return "Sorry, {player} not found."


@app.delete ("/players/{player_name}")
async def remove_player(player: Player):
    player = Player(name=player.name)    
    for player in players.items():
        if player.name == player.name:
            players.pop(player)
            return "{player} has been removed."
        return "Sorry, {player} not found."

## Courses
#@app.get("/courses")
#async def course_list() -> list[Course]:
#    return courses.values
#
#@app.post ("/players")
#async def create_player(player_detail: CreatePlayerRequest) -> uuid.UUID:
#    player_id = uuid.uuid4()
#    player = Player(id=player_id, name=player_detail.name, handicap=player_detail.handicap)
#    players[player_id] = player
#    return player.id
#
#@app.put ("/courses/{course_id}")
#async def update_course():
#    pass
#
#@app.delete ("/courses/{course_id}")
#async def remove_course():
#    pass