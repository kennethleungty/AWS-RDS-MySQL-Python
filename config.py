import pymysql

USERNAME = 'admin'  # Replace with your master username 
PASSWORD = 'XXXXX'  # Replace with your RDS instance password
ENDPOINT = "XXXXX.XXXXX.ap-southeast-1.rds.amazonaws.com"  # Replace with your RDS endpoint
PORT = 3306   # Replace with the RDS instance port
REGION = "ap-southeast-1"  # Replace with your AWS region
DBNAME = 'schema1'  # Replace with the name of your SCHEMA in MySQL workbench
SSL_CA = "ssl/rds-combined-ca-bundle.pem"  # Replace with the folder location of your SSL bundle
CURSORCLASS = pymysql.cursors.DictCursor  # No need to modify this
