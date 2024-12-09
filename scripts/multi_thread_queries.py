import pymysql
import threading

def insert_data():
    connection = pymysql.connect(
        host='automated-mysql-server-9019432.mysql.database.azure.com',
        user='rootdb',
        password='leesaroy@12345',
        database='project_db'
    )
    cursor = connection.cursor()
    insert_query = "INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, ("Kitchener", "2024-01-01", 28.0, 2.0, 70.0))
    connection.commit()
    cursor.close()
    connection.close()

def select_data():
    connection = pymysql.connect(
        host='automated-mysql-server-9019432.mysql.database.azure.com',
        user='rootdb',
        password='leesaroy@12345',
        database='project_db'
    )
    cursor = connection.cursor()
    select_query = "SELECT * FROM ClimateData WHERE temperature > 20.0"
    cursor.execute(select_query)
    results = cursor.fetchall()
    print(results)
    cursor.close()
    connection.close()

def update_data():
    connection = pymysql.connect(
        host='automated-mysql-server-9019432.mysql.database.azure.com',
        user='rootdb',
        password='leesaroy@12345',
        database='project_db'
    )
    cursor = connection.cursor()
    update_query = "UPDATE ClimateData SET humidity = 75.0 WHERE location = 'Toronto'"
    cursor.execute(update_query)
    connection.commit()
    cursor.close()
    connection.close()

threads = []
threads.append(threading.Thread(target=insert_data))
threads.append(threading.Thread(target=select_data))
threads.append(threading.Thread(target=update_data))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
