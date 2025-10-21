import os
import pandas as pd
import pyodbc
import sqlalchemy
import urllib


# Load data
try:
    brands = pd.read_csv('brand_detail.csv')
    spend = pd.read_csv('daily_spend.csv')
    print("✅ CSV files loaded successfully")
except Exception as e:
    print("❌ Failed to load CSVs:", e)
    raise

# Connect to Azure SQL
conn_str = (
    f"Driver={{ODBC Driver 18 for SQL Server}};"
    f"Server=tcp:day8exercise.database.windows.net,1433;"
    f"Database=Day8Exercise;"
    f"Uid=jenny;"
    f"Pwd=day8exercise!;"
    f"Encrypt=yes;"
    f"TrustServerCertificate=yes;"
    f"Connection Timeout=30;"
)

params = urllib.parse.quote_plus(conn_str)
engine = sqlalchemy.create_engine(f'mssql+pyodbc:///?odbc_connect={params}')

# Upload CSVs
try:
    print("📤 Uploading CSV data to Azure SQL...")
    brands.to_sql('BrandDetail', con=engine, if_exists='replace', index=False)
    spend.to_sql('DailySpend', con=engine, if_exists='replace', index=False)
    print("✅ Data uploaded successfully!")
except Exception as e:
    print("❌ Failed to upload data:", e)
    raise