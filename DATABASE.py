import numpy as np
import array
import sqlite3



conn=sqlite3.connect('PFMSDB.db')
c=conn.cursor()
c.execute("""SELECT * FROM PFMSDB""")
s=c.fetchall()
print("records in db are", s)
arr = np.array(s)
print(arr)