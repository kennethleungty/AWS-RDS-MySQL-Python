import pymysql

ACCESS_KEY_USER_KENNETH = 'xxxxx'
SECRET_KEY_USER_KENNETH = 'xxxxx'
USERNAME = 'admin' # Master username
PASSWORD = 'xxx' # Password of RDS Credential Settings
ENDPOINT = "client-database.xxxxx.ap-southeast-1.rds.amazonaws.com"
PORT = 3306
REGION = "ap-southeast-1"
DBNAME = "client-database"
CURSORCLASS = pymysql.cursors.DictCursor
SSL_CA = "ssl/ap-southeast-1-bundle.pem"