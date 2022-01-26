import mysql.connector


def connection():

    conn = mysql.connector.connect(
        host="localhost", user="root", password="@Archer#9810", database="fewing_view_database"
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
    return mycursor.fetchall()


if __name__ == "__main__":
    conn = connection()
    insert_into_table(conn, sql_query="", values=())
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)
