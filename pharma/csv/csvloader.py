import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime


import os
import importlib.util
HIDDEN_FILE_PATH = os.path.join('/home/agmt92/secure', 'hidden.py')
spec = importlib.util.spec_from_file_location("hidden", HIDDEN_FILE_PATH)
hidden = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hidden)
secrets = hidden.DB_Load()

Base = declarative_base()

class pharmas(Base):
    __tablename__ = 'pharmas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Pharmacy = Column(String(250))
    PharmacistName = Column(String(250))
    Mouhafaza = Column(String(250))
    Casa = Column(String(250))
    Address = Column(String(250))
    Phone = Column(String(250))




def load_csv_to_db(csv_file_path):
    DATABASE_URI = secrets["DATABASE_URI"]
    engine = create_engine(DATABASE_URI, echo=False, connect_args={"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"})

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Explicitly specify data types for pandas
    dtype_dict = {
 #       'Code': pd.Int64Dtype(),
 #       'price17424': pd.Int64Dtype(),
 #       'Pharmmarg': pd.Float64Dtype(),
 #       'PubDec': pd.Float64Dtype(),
 #       'Subsidy': pd.Float64Dtype(),
 #       # Add other fields as necessary
    }

    # Read the CSV with explicit types and date parsing
    df = pd.read_csv(csv_file_path, dtype=dtype_dict)

    # Convert the 'ExcDat' column to datetime, handling nulls
 #   df['ExcDat'] = pd.to_datetime(df['ExcDat'], errors='coerce')


    # Check the first few rows to ensure data types are loaded correctly
    print(df.dtypes)
    print(df.head())

    batch_size = 500
    for start_row in range(0, df.shape[0], batch_size):
        end_row = min(start_row + batch_size, df.shape[0])
        batch = df.iloc[start_row:end_row]

        # Ensure the columns in the dataframe match the model attribute names
        # For example:
        # batch.rename(columns={'RegNum': 'RegNum', 'BrandNam': 'BrandNam', ...}, inplace=True)

        data_to_insert = batch.to_dict(orient='records')

        session.bulk_insert_mappings(pharmas, data_to_insert)
        session.commit()
        print(f"Imported {end_row} entries into the database.")

    session.close()
    print("Data import completed successfully.")

csv_file_path = '/home/agmt92/django_projects/mysite/pharma/csv/check.csv'
load_csv_to_db(csv_file_path)
