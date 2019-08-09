import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='	id5162425_riya',
                             password='Yes',
                             db='id5162425_echallan',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:


    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `login` WHERE 1"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()