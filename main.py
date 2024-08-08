import csv
import mysql.connector
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="77312279",
    database="killme"
)
cursor = cnx.cursor()
def import_data(filename):
    csv_to_db_column_map = { #dictionary creation
        'work_year': 'work_year',
        'job_title': 'job_title',
        'job_category': 'job_category',
        'salary_currency': 'salary_currency',
        'salary': 'salary',
        'salary_in_usd': 'salary_in_usd',
        'employee_residence': 'employee_residence',
        'experience_level': 'experience_level',
        'employment_type': 'employment_type',
        'work_setting': 'work_setting',
        'company_location': 'company_location',
        'company_size': 'company_size'
    }
    with open(filename, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        insert_query = "INSERT INTO b (work_year, job_title, job_category, salary_currency, salary, salary_in_usd, employee_residence, experience_level, employment_type, work_setting, company_location, company_size) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for row in csvreader:
            db_row = [row[csv_to_db_column_map[col]] for col in csv_to_db_column_map.values()]
            cursor.execute(insert_query, tuple(db_row))
    cnx.commit()
    import_data("jobs_in_data.csv")