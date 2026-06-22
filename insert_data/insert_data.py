import mysql.connector
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

conn = mysql.connector.connect(
    host="mysql-21c6b9ea-myproject2024.g.aivencloud.com",
    port=15280,
    database="analytic_project",
    user="avnadmin",
    password = os.getenv("AIVEN_PASSWORD"),
    ssl_ca=r"C:\Users\steve\OneDrive\Desktop\college\Analytics_Project\ca.pem"
)

df = pd.read_csv(r"C:\Users\steve\Downloads\cleaned_dataset.csv")

# Fix duplicate columns automatically
df = df.loc[:, ~df.columns.duplicated()]

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()
print(f"Inserted {len(df)} rows successfully!")
cursor.close()
conn.close()