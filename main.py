import uuid

from fastapi import FastAPI

from models.player import Player
from models.course import Course


app = FastAPI()

players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}


# Players
@app.get("/players")
async def player_list():
#    pass
#
#@app.post ("/players")
#async def add_player ():
#    pass
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
#async def course_list():
#    pass
#
#@app.post ("/courses")
#async def add_course():
#    pass
#
#@app.put ("/courses/{course_id}")
#async def update_course():
#    pass
#
#@app.delete ("/courses/{course_id}")
#async def remove_course():
#    pass