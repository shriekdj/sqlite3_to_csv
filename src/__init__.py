# for CSV
import sqlite3
import os
import csv
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

SQL_DB = os.environ.get("SQL_DB")
OUTPUT_CSV = os.environ.get("OUTPUT_CSV")
TABLE_TO_EXPORT = os.environ.get("TABLE_TO_EXPORT")

# Connect to database
conn = sqlite3.connect(SQL_DB)

cursor = conn.cursor()

# # Create Table into database
# cursor.execute('''CREATE TABLE IF NOT EXISTS my_table(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
# 						name TEXT NULL, age INTEGER NULL);''')

# Export data into CSV file
def export_to_csv(sqlite3_file_path, csv_output_path, table_to_extract):
	# Connect to database
	conn = sqlite3.connect(SQL_DB)

	cursor = conn.cursor()

	print("Exporting data into CSV............")
	cursor.execute(f"SELECT * FROM {TABLE_TO_EXPORT}")
	with open(OUTPUT_CSV, "w", newline='', encoding='utf-8') as csv_file:
			csv_writer = csv.writer(csv_file, delimiter=",")
			csv_writer.writerow([i[0] for i in cursor.description])
			csv_writer.writerows(cursor)

	dirpath = os.getcwd() + "/" + OUTPUT_CSV
	print("Data exported Successfully into {}".format(dirpath))

if __name__ == "__main__":
	export_to_csv(SQL_DB, OUTPUT_CSV, TABLE_TO_EXPORT)
	cursor.close()
	conn.close()
