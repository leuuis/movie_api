from typing import List
from fastapi import APIRouter
from schemas.movie import Movie
from config.database import Session
from services.movie import MovieService
from fastapi.responses import JSONResponse
from middlewares.jwt_bearer import JWTBearer
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from fastapi import Depends, Path, Query, status

movie_router = APIRouter()

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Avatar 2",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.9,
        "category": "Acción"
    }
]

@movie_router.get('/movies', tags=['Movies'], response_model=List[Movie], status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(content= jsonable_encoder(result), status_code=status.HTTP_200_OK)

@movie_router.get('/movies/{id}', tags=['Movies'], response_model=Movie, status_code=status.HTTP_200_OK)
def get_movie(id: int = Path(le=2000, ge=1)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(content={'message:' "No encontrado"}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@movie_router.get('/movies/', tags=['Movies'], response_model=List[Movie], status_code=status.HTTP_200_OK)
def get_movies(category: str = Query(max_length=15, min_length=5)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(content={'message:' "No encontrado"}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@movie_router.post('/movies', tags=['Movies'], response_model=dict, status_code=status.HTTP_201_CREATED)
def create_movie(
    movie: Movie
) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})

@movie_router.put('/movies/{id}', tags=['Movies'], response_model=dict, status_code=status.HTTP_200_OK)
def update_movie(
    id: int,
    movie: Movie
) -> dict:
    db = Session()
    result = MovieService.get_movie(id)
    if not result:
        return JSONResponse(content={'message:' "No encontrado"}, status_code=status.HTTP_404_NOT_FOUND)
            
    MovieService(db).update_movie(id, movie)
    return JSONResponse(content={"message": "Se ha actualizado la película"}, status_code=status.HTTP_200_OK)

@movie_router.delete('/movies/{id}', tags=['Movies'], response_model=dict, status_code=status.HTTP_200_OK)
def delete_movie(id: int) -> dict:
    db = Session()
    result = MovieService.get_movie(id)
    if not result:
        return JSONResponse(content={'message:' "No encontrado"}, status_code=status.HTTP_404_NOT_FOUND)
    MovieService(db).delete_movie(id)
    return JSONResponse(content={"message": "Se ha eliminado la película"}, status_code=status.HTTP_200_OK)