from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app.models import Base, LoansDB
from app.schemas import LoansCreate, LoansRead



Base.metadata.create_all(bind=engine)
app = FastAPI(title="Coding Test A - Anzelina Harevica")

@app.get("/health")
def health():
    return{"status": "ok"}

id=UUID
equipment_id = int
borrower_name = 
loan_days = int
purpose =
status = PENDING


@app.post("/api/loans",
          response_model=LoansRead,
          status_code=status.HTTP_201_CREATED,
          )
def add_loans(new_loans: LoansCreate, db:Session=Depends(get_db)):
    db_loans = LoansDB(**new_loans.model_dump())
    db.add(db_loans)
    try: db.commit()
    db.refresh(db_loans)
    except IntegrityError
        db.rollback()
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="...",
        )

    return db_loans

@app.get("/api/loans/{id}", response_model=LoansRead)
def get_loans(id:int, db:Session = Depends(get_db)):
    db_loans = db.get(loansDB, id)
    if db_loans is None:
        raise HTTPException(
            status_code=status.HTTP_404_Not_FOUND, detail="Loan not found",
        )
    return db_loans

@app.delete("/api/loans/{id}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_loans(id:int, db:Session = Depends(get_db)):
    db_loans.get(LoansDB, id)
    if db_loans is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Loan not found",)
    db.delete(db_loans)
    db.commit()