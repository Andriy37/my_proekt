from db import crud, models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/departments/", response_model=schemas.Department)
def create_department(department: schemas.DepartmentCreate, db:Session=Depends(get_db)):
    return crud.create_department(db=db, department=department)

