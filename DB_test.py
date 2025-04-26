import mysql.connector
from datetime import datetime

# Connect to MySQL database
conn = mysql.connector.connect(
    host="sql8.freesqldatabase.com",         # or "127.0.0.1"
    user="sql8775439",     # replace with your MySQL username
    password="Xx49cXD2lT", # replace with your MySQL password
    database="sql8775439"  # replace with your DB name
)

cursor = conn.cursor()

# Create gardendata table
create_gardendata = """
CREATE TABLE IF NOT EXISTS gardendata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    temperature FLOAT,
    soil_moisture FLOAT,
    humidity FLOAT
)
"""
cursor.execute(create_gardendata)

# Create gemini_data table
create_gemini_data = """
CREATE TABLE IF NOT EXISTS gemini_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    response TEXT,
    garden_health VARCHAR(100),
    fertilizer VARCHAR(100)
)
"""
cursor.execute(create_gemini_data)

conn.commit()
cursor.close()
conn.close()

print("Tables created successfully.")
