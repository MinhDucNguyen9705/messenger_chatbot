import sqlite3
import csv

# Replace 'your_database.db' with the actual database name
database_name = 'diem_thi_thpt_2023.db'
csv_file_path = 'diem_thi_thpt_2023_cleaned.csv'

# Connect to the SQLite database
connection = sqlite3.connect(database_name)
cursor = connection.cursor()

# Create a table (modify the table structure based on your CSV)
cursor.execute('''CREATE TABLE IF NOT EXISTS diem_thi_thpt_2023(
                    sbd INTEGER PRIMARY KEY,
                    Toan REAL,
                    Ngu_Van REAL,
                	Ngoai_Ngu REAL, 
                    Vat_Ly REAL, 
                    Hoa_Hoc REAL,
                    Sinh_Hoc REAL,
                    Lich_Su REAL,
                    Dia_Li REAL,
                    GDCD_REAL,
                    MA_NGOAI_NGU VARCHAR(3),
                    B00 REAL,
                    C00 REAL,
                    A00 REAL,
                    D00 REAL,
                    A01 REAL
                 )''')

# Read data from CSV and insert into the database
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header if it exists

    for row in csv_reader:
        cursor.execute('INSERT INTO diem_thi_thpt_2023 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(row))

# Commit changes and close the connection
connection.commit()
connection.close()