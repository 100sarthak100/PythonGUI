import sqlite3
def createTable():
    conn = sqlite3.connect("login.db")
    #conn.execute("CREATE TABLE SAT (Sattelite TEXT NOT NULL,TargetAzimuth int , TargetElevation int)")

    #conn.execute("INSERT INTO SAT VALUES(?,?,?)",('SAT-4',16,16 ))

    #conn.commit()
    result = conn.execute("SELECT * FROM SAT")


    for data in result:
        print("Satellite : ", data[0])
        print("TargetAzimuth : ", data[1])
        print("TargetElevation : ", data[2])

    conn.close()


createTable()