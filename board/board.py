import logging
from fastapi import APIRouter, Request, Body, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


# DB
from sqlalchemy.orm import Session
from board import crud, model, schemas
from .database import SessionLocal, engine

# router
router = APIRouter()

# templates
templates = Jinja2Templates(directory="./board/templates")

# db engine
model.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("", response_class=HTMLResponse)
async def board_view(request: Request):
    db = next(get_db())
    boards = crud.get_boards(db)

    return templates.TemplateResponse("index.html", {"request": request,
                                                     "boards": list(boards)
                                                     }
                                      )


@router.get("/all", response_model=schemas.Board)
async def get_boards(db: Session = Depends(get_db)):
    return crud.get_board_by_id(db, 1)


@router.post("", response_model=schemas.Board)
async def create(title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    board = schemas.BoardCreate
    board.title = title
    board.content = content
    print('db create')
    return crud.create_board(db=db, board=board)


@router.delete("/{board_id}")
async def delete(board_id: int, db: Session = Depends(get_db)):
    crud.delete_board(db=db, board_id=board_id)
    response = {
        "msg": "ok"
    }

    return response
