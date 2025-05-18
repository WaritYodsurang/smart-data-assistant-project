import pandas as pd
import duckdb
from datetime import datetime

# Step 1: Load dataset
csv_path = "data/superstore_sales.csv"
df = pd.read_csv(csv_path)

# Step 2: Connect to DuckDB
con = duckdb.connect("smart_data.duckdb")

# Step 3: Create or replace table
con.execute("DROP TABLE IF EXISTS sales")
con.execute("CREATE TABLE sales AS SELECT * FROM df")

# Step 4: Print summary
print(f"[{datetime.now()}] ✅ Loaded {len(df)} records into 'sales' table in smart_data.duckdb.")
