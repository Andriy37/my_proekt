from sqlalchemy.orm import Session
from.import models, schemas

def get_department(db: Session, department_id: int):
    return db.query(models.Department).filter(models.Department.id==department_id).first()

def get_departmens(db:Session, skip: int=0, limit: int = 100):
    return db.query(models.Department).offset(skip).limit(limit).all()

def create_department(db:Session, department:schemas.DepartmentCreate):
    db_department = models.Department(name = department.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)

def get_employee(db:Session, skip:int=0, limit:int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_department_product(db:Session, product:schemas.ProductCreate, department_id:int):
    db_product = models.Product(**product.model_dump(), department_id=department_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product