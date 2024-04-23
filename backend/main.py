from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import Movie


movies: list[Movie] = [
    Movie(movie_id=239, name="Spider-Man", year=2002),
    Movie(movie_id=561, name="Thor: Ragnarok", year=2017),
    Movie(movie_id=125, name="Iron Man", year=2008),
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # The origin of the frontend app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
