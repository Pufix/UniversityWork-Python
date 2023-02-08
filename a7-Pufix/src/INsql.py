import mysql.connector
from domain import book
def loading(username,pswrd):
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user=username,
          password=pswrd,
          database="library"
        )
    except:
        raise ValueError("ERROR: Cannot connect to SQL!")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM books")
    myresult = mycursor.fetchall()
    array=[]
    for x in myresult:
        dictio={}
        dictio['uuid']=x[0]
        dictio['name']=x[1]
        dictio['author']=x[2]
        array.append(book(dictio))
    return array