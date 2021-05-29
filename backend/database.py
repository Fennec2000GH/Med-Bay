
import mariadb, os, sys
from dotenv import load_dotenv

load_dotenv()
USERNAME_DB = os.getenv(key='USERNAME_DB')
PASSWORD_DB = os.getenv(key='PASSWORD_DB')
DB = os.getenv(key='DB')

try:
	conn = mariadb.connect(
		user=USERNAME_DB,
		password=PASSWORD_DB,
		host='localhost',
		port=3306,
		database=DB
	)
except mariadb.Error as error:
	print(error)
	sys.exit(1)

cur = conn.cursor()

