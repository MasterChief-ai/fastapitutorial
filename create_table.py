from database import Base, engine
import model

Base.metadata.create_all(bind=engine) # calling mysql to create the tables in model.py

