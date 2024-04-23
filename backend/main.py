import uuid

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import (
    Movie,
    CreateMovieRequest,
    CreateMovieResponse,
    UpdateMovieRequest,
    UpdateMovieResponse,
    DeleteMovieResponse,
)


movies: list[Movie] = [
    Movie(movie_id=uuid.uuid4(), name="Spider-Man", year=2002),
    Movie(movie_id=uuid.uuid4(), name="Thor: Ragnarok", year=2017),
    Movie(movie_id=uuid.uuid4(), name="Iron Man", year=2008),
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/movies")
async def get_movies() -> list[Movie]:
    raise NotImplementedError

@app.post("/movies")
async def create_movie(new_movie: CreateMovieRequest) -> CreateMovieResponse:
    raise NotImplementedError

@app.put("/movies/{movie_id}")
async def update_movie(movie_id: uuid.UUID, updated_movie: UpdateMovieRequest) -> UpdateMovieResponse:
    raise NotImplementedError

@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: uuid.UUID) -> DeleteMovieResponse:
    raise NotImplementedError