from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='reality_pc'

mysql=MySQL(app)
mysql.init_app(app)
from shopping import routes


