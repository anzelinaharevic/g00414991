from fastapi import Depends, FastAPI

app = FastAPI(title="Example template")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.get("/api/loans/{id}"
        response_model=LoansRead)
def get_loans(id:int, db:Session = Depends(get_db)):
    db_loan = db.get(loansDB, id)
    if db_loans is None:
        raise HTTPException(
            status_code=status.HTTP_404_Not_FOUND, detail="Loan not found",
        )
    return db_loan