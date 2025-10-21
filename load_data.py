import pandas as pd
import pyodbc
import sqlalchemy

# Load data
brands = pd.read_csv('brand_detail.csv')
spend = pd.read_csv('daily_spend.csv')

# Connect to Azure SQL
conn_str = 'Server=tcp:day8exercise.database.windows.net,1433;Initial Catalog=Day8Exercise;Persist Security Info=False;User ID=jenny;Password=day8exercise!;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;'
engine = sqlalchemy.create_engine(f'mssql+pyodbc:///?odbc_connect={conn_str}')

# Load tables
brands.to_sql('BrandDetail', con=engine, if_exists='replace', index=False)
spend.to_sql('DailySpend', con=engine, if_exists='replace', index=False)

print("✅ Data uploaded successfully!")