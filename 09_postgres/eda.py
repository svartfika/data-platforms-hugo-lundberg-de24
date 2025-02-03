import os
from pathlib import Path

import dotenv
import pandas as pd
from sqlalchemy import create_engine

dotenv.load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")

db_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
conn_postgres = create_engine(db_url)

path_data = Path(__file__).parent / "resultat-ansokningsomgang-2024.xlsx"
df = pd.read_excel(path_data, sheet_name="Tabell 3", skiprows=5)

df.columns = df.columns.str.lower().str.replace(" ", "_")

df.to_sql("myh_2024", conn_postgres, schema="public", if_exists="replace", index=False)
