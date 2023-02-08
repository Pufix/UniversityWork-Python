import mysql.connector
from domain import book
def pushing(array,mods,username,pswrd):
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
    while len(mods)>0:
        if mods[0][0]=='add':
            sql="INSERT INTO `books` (`uuid`, `name`, `author`) VALUES (%s,%s,%s)"
            val = (array[mods[0][1]].uuid,array[mods[0][1]].name,array[mods[0][1]].author)
            mycursor.execute(sql, val)
            mydb.commit()
        elif mods[0][0]=='filter':
            letter=[]
            for i in mods[0][1]:
                letter=i[0].get_first_letter()
                break
            sql = "DELETE FROM books WHERE name LIKE '"+ letter +"%'"
            empty=[]
            mycursor.execute(sql,empty)
            sql = "DELETE FROM books WHERE name LIKE '"+ letter.lower() +"%'"
            empty=[]
            mycursor.execute(sql,empty)
            sql = "DELETE FROM books WHERE name LIKE '"+ letter.upper() +"%'"
            empty=[]
            mycursor.execute(sql,empty)
            mydb.commit()
        mods.pop(0)
