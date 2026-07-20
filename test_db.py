from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    try:
        result = db.execute("SELECT 1;")
        return {"db_ok": True, "result": list(result)}
    except Exception as e:
        return {"db_ok": False, "error": str(e)}
