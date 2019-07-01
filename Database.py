import sqlite3
def createTable():
    conn = sqlite3.connect("login.db")

    #conn.execute("CREATE TABLE USERS (USERNAME TEXT NOT NULL , USERID int , PASSWORD int)")

    #conn.execute("INSERT INTO USERS VALUES(?,?,?)",('sarthak',1234,1234))

    #conn.commit()

    result = conn.execute("SELECT * FROM USERS")

    for data in result:
        print("USERNAME : ",data[0])
        print("USER ID : ",data[1])
        print("PASSWORD : ",data[2])

    conn.close()

createTable()