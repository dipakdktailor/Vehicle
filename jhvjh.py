import pymysql
import sys
from PIL import Image
import base64
import io.cStringIO as ak
import PIL.Image

db=pymysql.connect("localhost","root","","vehicle")
cursor=db.cursor()

image = Image.open('C:\Users\dtail\Downloads\2.jpg','rb')
blob_value = open('C:\Users\dtail\Downloads\2.jpg', 'rb').read()
sql = 'INSERT INTO img(images) VALUES(%s)'
args = (blob_value, )
cursor=db.cursor()
cursor.execute(sql,args)
sql1='select * from img'
db.commit()
cursor.execute(sql1)
data=cursor.fetchall()
print(type(data[0][0]))
file_like=ak.StringIO(data[0][0])
img=PIL.Image.open(file_like)
img.show()

db.close()