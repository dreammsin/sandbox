import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

sqlstring = input("Enter sql:")
mycursor = mydb.cursor()

mycursor.execute("$sqlstring")

print("Hello from python")

## Enter fake secrets
user = "careless@oops.com"
password = ";|F41;uF63HJociypn~y"
oid = "2436-BCC5-9A6D-1579-D57A"
## user notified
azure_sas_token = "M1TdXiipdLqD6HW9ermS"
## validation notified
github_oauth_access_token = "M1TdXiipdLqD6HW9ermS"
azure_storage_account_key="SoK0BArf8LPIMIlx4CUZPyFfZ4bDi+vx/IYhjKTMK+ZHIwR8DAC7aasxrfIuFo7YBmQbL5wwwXcA+AStePxzNA=="

x = int(20)
x = range(6)

from django.db import connection

def show_user(request, username):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)