from sqlalchemy.orm import Session

from . import model as models, schemas


def get_boards(db: Session):
    return db.query(models.Board).all()


def get_board_by_id(db: Session, board_id: int):
    return db.query(models.Board).filter(models.Board.id == board_id).first()


def create_board(db: Session, board: schemas.BoardCreate):
    db_board = models.Board(title=board.title, content=board.content)
    db.add(db_board)
    db.commit()
    db.refresh(db_board)
    return db_board


def delete_board(db: Session, board_id: str):
    board_id = int(board_id)
    db_board = db.query(models.Board).filter(models.Board.id == board_id).first()

    try:
        db.delete(db_board)
        db.commit()
        db.refresh()
    except:
        return {"msg": "fail"}

    return {"msg": "success"}
