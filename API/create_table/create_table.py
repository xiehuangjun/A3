import pymysql, json, configparser, os, datetime

from pymysql.connections import DEFAULT_CHARSET

path = os.path.abspath('.')
cfgpath = path.split('A3/API')[0] + 'A3/API/config.ini'

config = configparser.ConfigParser()
config.read(cfgpath)

mysql = pymysql.connect(user = config["MYSQL"]["user"], password = config["MYSQL"]["password"], port = int(config["MYSQL"]["port"]), host = config["MYSQL"]["host"])
cur = mysql.cursor()

cur.execute('''CREATE DATABASE User;''')

cur.execute('''CREATE TABLE IF NOT EXISTS User.information (
                User_account CHAR(50),
                User_password CHAR(50),
                User_cellphone CHAR(50),
                User_email CHAR(50),
                User_city CHAR(50)
            )ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;''')

mysql.commit()
cur.close()