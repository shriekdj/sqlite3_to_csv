# for CSV
import sqlite3
import os
import csv

SQL_DB = "./sqlite_input.db"
TABLE_TO_EXPORT = "my_table"
OUTPUT_CSV = "csv_output.csv"

# Connect to database
conn = sqlite3.connect(SQL_DB)

cursor = conn.cursor()

# Create Table into database
cursor.execute('''CREATE TABLE IF NOT EXISTS my_table(Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
						name TEXT NULL, age INTEGER NULL);''')

# Export data into CSV file
def export_to_csv():
	print("Exporting data into CSV............")
	cursor.execute(f"SELECT * FROM {TABLE_TO_EXPORT}")
	with open(OUTPUT_CSV, "w", newline='', encoding='utf-8') as csv_file:
			csv_writer = csv.writer(csv_file, delimiter=",")
			csv_writer.writerow([i[0] for i in cursor.description])
			csv_writer.writerows(cursor)

	dirpath = os.getcwd() + "/" + OUTPUT_CSV
	print("Data exported Successfully into {}".format(dirpath))

if __name__ == "__main__":
	export_to_csv()
	cursor.close()
	conn.close()
