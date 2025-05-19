from typing import Union
from pydantic import BaseModel

class ProductBase(BaseModel):
    title: str
    description: Union[str, None] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    department_id: int
    class Config:
        from_attributes = True

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    products: list[Product] = []
    
    class Config:
        from_attributes = True