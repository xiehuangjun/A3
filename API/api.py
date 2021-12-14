import pymysql, json, configparser, os, base64
from flask import Flask, config, request, jsonify
from flask_cors import cross_origin
from flask_api import status

path = os.path.abspath('.')
cfgpath = path.split('A3/API')[0] + 'A3/API/config.ini'

config = configparser.ConfigParser()
config.read(cfgpath)

app = Flask(__name__)

@app.route('/register', methods = ['POST'])
@cross_origin()
def register():
    mysql = pymysql.connect(user = config['MYSQL']["user"], password = config['MYSQL']["password"], port = int(config['MYSQL']["port"]), host = config['MYSQL']["host"])
    cur = mysql.cursor()

    data_json = {}
    
    cur.execute('''SELECT * FROM User.information WHERE User_account = '%s';''' %request.form.get('User_account'))
    data = cur.fetchall()

    if(len(data) != 0):
        data_json['Log'] = "Account already used"
        return json.dumps(data_json), status.HTTP_400_BAD_REQUEST
    else:
        INSERT = '''INSERT INTO User.information (
                                        User_account, 
                                        User_password, 
                                        User_cellphone, 
                                        User_email, 
                                        User_city
                                        ) VALUES( %s, %s, %s, %s, %s);'''
        insert_data = (
            request.form.get('User_account'),
            request.form.get('User_password'),
            request.form.get('User_cellphone'),
            request.form.get('User_email'),
            request.form.get('User_city')
           )
        
        cur.execute(INSERT, insert_data)
        mysql.commit()
        data_json['Log'] = "Register Success"
        return json.dumps(data_json), status.HTTP_200_OK

@app.route('/login', methods = ['POST'])
@cross_origin()
def login():
    mysql = pymysql.connect(user = config['MYSQL']["user"], password = config['MYSQL']["password"], port = int(config['MYSQL']["port"]), host = config['MYSQL']["host"])
    cur = mysql.cursor()
    data_json = {}
    
    User_account = request.form.get('User_account')
    User_password = request.form.get('User_password')

    cur.execute('''SELECT * FROM User.information WHERE User_account = '%s';''' %User_account)
    data = cur.fetchall()
    
    if(len(data) == 0):
        data_json['Log'] = "Account didn't register"
        return json.dumps(data_json), status.HTTP_400_BAD_REQUEST
    else:
        if(data[0][1] != User_password):
            data_json['Log'] = "Login Filed"
            return json.dumps(data_json), status.HTTP_400_BAD_REQUEST
        else:
            data_json['Log'] = "Login Success"
            return json.dumps(data_json), status.HTTP_200_OK


app.run(host = config['FLASK']['host'], port = int(config['FLASK']['port']), debug=True )

