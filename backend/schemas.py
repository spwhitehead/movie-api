from pydantic import BaseModel


class Movie(BaseModel):
    movie_id: int
    name: str
    year: int