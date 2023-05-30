import pymysql
db=pymysql.connect("localhost","root","","ct_python")
cursor=db.cursor()
#to take input from user
pname=input("enter the product name")
quantity=int(input("enter the quantity"))
price=int(input("enter the price"))
barcode=input("enter the barcode number")
try:
    sql="callsproductInsert"("%s","%d","%f","%s")