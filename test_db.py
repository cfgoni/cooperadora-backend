from fastapi import APIRouter
from database import engine

router = APIRouter()

@router.get("/db-test")
def db_test():
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT 1;")
            return {"db_ok": True, "result": list(result)}
    except Exception as e:
        return {"db_ok": False, "error": str(e)}
