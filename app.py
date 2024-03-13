from flask import Flask , render_template , request , jsonify

app = Flask(__name__)

@app.route('/')
def productauthenticity():
    return render_template('index.html')

@app.route('/login')
def displaytheloginpage():
    return render_template('login.html')

@app.route('/dashboard')
def distributorsdb():
    return render_template('distributorsdb.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



























































































