import pymysql

connection = pymysql.connect(
    host='automated-mysql-server-9019432.mysql.database.azure.com',
    user='rootdb',
    password='leesaroy@12345',
    database='project_db'
)

cursor = connection.cursor()

sample_data = [
    ("Toronto", "2024-01-08", 9.0, 11.0, 66.0),
    ("Waterloo", "2024-10-01", 17.0, 0.0, 55.0),
]

insert_query = "INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(insert_query, sample_data)

connection.commit()
cursor.close()
connection.close()
