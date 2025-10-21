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
conn_str = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:day8exercise.database.windows.net,1433;Initial Catalog=Day8Exercise;Persist Security Info=False;User ID=jenny;Password=day8exercise!;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;'
params = urllib.parse.quote_plus(conn_str)
engine = sqlalchemy.create_engine(f'mssql+pyodbc:///?odbc_connect={params}')

# Test connection
try:
    print("🔗 Testing connection to Azure SQL...")
    with engine.connect() as conn:
        result = conn.execute("SELECT 1").fetchone()
        print("✅ Connection successful, test query result:", result)
except Exception as e:
    print("❌ Connection failed:", e)
    raise

# Upload CSVs
try:
    print("📤 Uploading CSV data to Azure SQL...")
    brands.to_sql('BrandDetail', con=engine, if_exists='replace', index=False)
    spend.to_sql('DailySpend', con=engine, if_exists='replace', index=False)
    print("✅ Data uploaded successfully!")
except Exception as e:
    print("❌ Failed to upload data:", e)
    raise