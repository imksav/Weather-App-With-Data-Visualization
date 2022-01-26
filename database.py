import mysql.connector


def connection():
    conn = mysql.connector.connect(
        host="localhost", user="root", password="root", database="fewing_view_database"
    )
    return conn


def insert_into_table(conn, sql_query, values):
    mycursor = conn.cursor()
    mycursor.execute(sql_query, values)
    conn.commit()
    print("insertion sucessfull")


def select_from_table(conn, sql_query):
    mycursor = conn.cursor()
    mycursor.execute(sql_query)
    all_data = mycursor.fetchall()
    return all_data
    # print(mycursor.fetchall())
    # for item in all_data:
    #         city = item[1]
    #         lat = item[2]
    #         lon = item[3]
    #         temp = item[4]
    #         img = item[5]
            
            # print(city, lat, lon, temp, img)

if __name__ == "__main__":
    conn = connection()
    insert_into_table(conn, sql_query="", values=())
    select_from_table(conn, "SELECT * FROM general_info")
    # select_from_table(conn, "SELECT * FROM general_info WHERE location_name='Butwal'")
    # print(data)
    # val = myfunc(data)
    # print(val)
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)
