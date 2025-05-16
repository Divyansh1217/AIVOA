from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
import uvicorn

# Correct import from models
from model import Company, Base
# SQLite database
DATABASE_URL = "sqlite:///./companies.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Pydantic schema
class CompanyCreate(BaseModel):
    id: int
    name: str
    address: str

# FastAPI instance
app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    # allow_origins=["*"],  # Uncomment for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST endpoint to create company
@app.post("/company")
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = db.query(Company).filter(Company.name == company.name).first()
    if db_company:
        raise HTTPException(status_code=400, detail="Company already exists")
    new_company = Company(id=company.id, name=company.name, address=company.address)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

# GET endpoint to read all companies
@app.get("/company", response_model=list[CompanyCreate])
def read_companies(db: Session = Depends(get_db)):
    companies = db.query(Company).all()
    if not companies:
        raise HTTPException(status_code=404, detail="No companies found")
    return companies

# Only used if running this file directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

