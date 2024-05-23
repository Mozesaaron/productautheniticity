# from flask import Flask, render_template, request, jsonify
# from flask_sqlalchemy import SQLAlchemy

# #postgres://liferootsmanagementdb_user:OAMWgGwc0N00mJgeqHCMaJdnweJpOrhx@dpg-cp2ubskf7o1s73bnudd0-a.oregon-postgres.render.com/liferootsmanagementdb

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://liferootsmanagementdb_user:OAMWgGwc0N00mJgeqHCMaJdnweJpOrhx@dpg-cp2ubskf7o1s73bnudd0-a.oregon-postgres.render.com/liferootsmanagementdb'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# @app.route('/hello')
# def hello():
#     return "Hello, Flask!"

# class Supervisors(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     names = db.Column(db.String(30))
#     grade = db.Column(db.String(5))

# # Ensure database tables are created within the application context
# with app.app_context():
#     db.create_all()

# def insertdata():
#     newsupervisor = Supervisors(names="mpanga moses", grade="Seven Star")
#     db.session.add(newsupervisor)
#     db.session.commit()

# @app.route('/')
# def addnumbers():
#     sp = Supervisors.query.all()
#     return render_template('index.html', sp=sp)

# @app.route('/getthesum', methods=['POST'])
# def thesumresult():
#     data = request.get_json()
#     num1 = int(data.get('num1'))
#     num2 = int(data.get('num2'))
#     result = num1 + num2
#     return jsonify({'result': result})

# if __name__ == '__main__':
#     insertdata
#     app.run(host='0.0.0.0', port=8080)

import psycopg2
from psycopg2 import OperationalError
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def grade7_table(connection):
    grade7_table_query = '''  CREATE TABLE IF NOT EXISTS grade7table(
        id SERIAL PRIMARY KEY,
        names VARCHAR(20)
    )  '''
    try:
        cursor = connection.cursor()
        cursor.execute(grade7_table_query)
        connection.commit()
        print("Table 'grade7_table' created successfully")
        cursor.close()
    except OperationalError as error:
        print(f"The error '{ error }' occured during grade7_table creation. ")

def grade8_table(connection):
    grade8_table_query = '''  CREATE TABLE IF NOT EXISTS grade8table(
        id SERIAL PRIMARY KEY,
        names VARCHAR(20)
    )  '''
    try:
        cursor = connection.cursor()
        cursor.execute(grade8_table_query)
        connection.commit()
        print("Table 'grade8_table' created successfully")
        cursor.close()
    except OperationalError as error:
        print(f"The error '{ error }' occured during grade8_table creation. ")

def grade9_table(connection):
    grade9_table_query = '''  CREATE TABLE IF NOT EXISTS grade9table(
        id SERIAL PRIMARY KEY,
        names VARCHAR(20)
    )  '''
    try:
        cursor = connection.cursor()
        cursor.execute(grade9_table_query)
        connection.commit()
        print("Table 'grade9_table' created successfully")
        cursor.close()
    except OperationalError as error:
        print(f"The error '{ error }' occured during grade9_table creation. ")

def grade10_table(connection):
    grade10_table_query = '''  CREATE TABLE IF NOT EXISTS grade10table(
        id SERIAL PRIMARY KEY,
        names VARCHAR(20)
    )  '''
    try:
        cursor = connection.cursor()
        cursor.execute(grade10_table_query)
        connection.commit()
        print("Table 'grade10_table' created successfully")
        cursor.close()
    except OperationalError as error:
        print(f"The error '{ error }' occured during grade10_table creation. ")

def grade11_table(connection):
    grade11_table_query = '''  CREATE TABLE IF NOT EXISTS grade11table(
        id SERIAL PRIMARY KEY,
        names VARCHAR(20)
    )  '''
    try:
        cursor = connection.cursor()
        cursor.execute(grade11_table_query)
        connection.commit()
        print("Table 'grade11_table' created successfully")
        cursor.close()
    except OperationalError as error:
        print(f"The error '{ error }' occured during grade11_table creation. ")

def grade12_table(connection):
    grade12_table_query = '''  CREATE TABLE IF NOT EXISTS grade12table(
        id SERIAL PRIMARY KEY,
        names VARCHAR(20)
    )  '''
    try:
        cursor = connection.cursor()
        cursor.execute(grade12_table_query)
        connection.commit()
        print("Table 'grade12_table' created successfully")
        cursor.close()
    except OperationalError as error:
        print(f"The error '{ error }' occured during grade12_table creation. ")

def grade6_table(connection):
    grade6_table_query = '''  CREATE TABLE IF NOT EXISTS grade6table(
        id SERIAL PRIMARY KEY,
        names VARCHAR(20)
    )  '''
    try:
        cursor = connection.cursor()
        cursor.execute(grade6_table_query)
        connection.commit()
        print("Table 'grade6_table' created successfully")
        cursor.close()
    except OperationalError as error:
        print(f"The error '{ error }' occured during grade6_table creation. ")

def grade5_table(connection):
    grade5_table_query = ''' CREATE TABLE IF NOT EXISTS grade5table(
        id SERIAL PRIMARY KEY,
        names VARCHAR(20)
    )  '''
    try:
        cursor = connection.cursor()
        cursor.execute(grade5_table_query)
        connection.commit()
        print("Table 'grade5_table' created successfully")
        cursor.close()
    except OperationalError as error:
        print(f"The error '{ error }' occured during grade5_table creation. ")

def grade2_table(connection):
    grade2_table_query = '''
    CREATE TABLE IF NOT EXISTS grade2table(
        id SERIAL PRIMARY KEY,
        names VARCHAR(20)
    )
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(grade2_table_query)
        connection.commit()
        print("Table 'grade2_table' created successfully")
        cursor.close()
    except OperationalError as error:
        print(f"The error '{error}' occurred during grade2_table creation. ")

def grade4_table(connection):
    grade4_table_query = '''
        CREATE TABLE IF NOT EXISTS grade4table(
        id SERIAL PRIMARY KEY,
        names VARCHAR(20)
        )
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(grade4_table_query)
        connection.commit()
        print("Table 'grade4_table' created successfully ")
        cursor.close()
    except OperationalError as error:
        print(f"The error '{ error }' ocurred during grade4_table creation. ")

def supervisors_table(connection):
    supervisors_table_query = '''
    CREATE TABLE IF NOT EXISTS supervisors (
        id SERIAL PRIMARY KEY,
        names VARCHAR(100) NOT NULL,
        grade VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(supervisors_table_query)
        connection.commit()
        print("Table 'supervisors' created successfully")
        cursor.close()
    except OperationalError as e:
        print(f"The error '{e}' occurred during table creation")

def insert_data(connection):
    insert_data_query = '''
    INSERT INTO supervisors (names, grade) VALUES (%s, %s)
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(insert_data_query, ('MPANGA MOSES', 'NINE'))
        connection.commit()
        print("Supervisor created successfully")
        cursor.close()
    except OperationalError as e:
        print(f"The error '{e}' occurred during Supervisor creation")

# Replace these values with your database credentials
db_name = "liferootsmanagementdb"
db_user = "liferootsmanagementdb_user"
db_password = "OAMWgGwc0N00mJgeqHCMaJdnweJpOrhx"
db_host = "dpg-cp2ubskf7o1s73bnudd0-a.oregon-postgres.render.com"
db_port = "5432"

# Test the connection and create the table
connection = create_connection(db_name, db_user, db_password, db_host, db_port)

# @app.route('/')
# def addnumbers():
#     sp = Supervisors.query.all()
#     return render_template('index.html', sp=sp)

@app.route('/')
def loginpage():
    return render_template('login.html')

if __name__ == '__main__':
    if connection is not None:
        supervisors_table(connection)  # Create the table if it doesn't exist
        grade2_table(connection)
        grade4_table(connection)
        grade5_table(connection)
        grade6_table(connection)
        grade7_table(connection)
        grade8_table(connection)
        grade9_table(connection)
        grade10_table(connection)
        grade11_table(connection)
        grade12_table(connection)
        #insert_data(connection)   # Insert data into the table
        connection.close()
        app.run(host='0.0.0.0', port=8080)


















































