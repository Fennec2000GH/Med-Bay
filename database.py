
import mariadb, os, sys
from graphene import ObjectType, String
from dotenv import load_dotenv

load_dotenv()
USERNAME_DB = os.getenv(key='USERNAME_DB')
PASSWORD_DB = os.getenv(key='PASSWORD_DB')

try:
	conn = mariadb.connect(
		user=USERNAME_DB,
		password=PASSWORD_DB,
		host='localhost',
		port=3306,
		database='test'
	)
except mariadb.Error as error:
	print(error)
	sys.exit(1)

cur = conn.cursor()

