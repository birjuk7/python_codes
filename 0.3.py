import psycopg2

try:
   connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="school")

   print("Selecting rows from mobile table using cursor.fetchall")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select * from company"

   cursor.execute(postgreSQL_select_Query)
   mobile_records = cursor.fetchmany(2)
   
   print("Printing 2 rows")
   for row in mobile_records:
       print("name = ", row[0], )
       print("place = ", row[1])
       print("age  = ", row[2], "\n")

   mobile_records = cursor.fetchmany(2)
   
   print("Printing next 2 rows")
   for row in mobile_records:
       print("name = ", row[0], )
       print("place = ", row[1])
       print("age  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
