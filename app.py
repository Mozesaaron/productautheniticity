from flask import Flask , render_template , request , jsonify

app = Flask(__name__)

@app.route('/')
def addnumbers():
    return render_template('index.html')

@app.route('/getthesum',  methods=['POST'])
def thesumresult():
        data = request.get_json()
        num1 = int(data.get('num1'))
        num2 = int(data.get('num2'))
        result = num1 + num2
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



























































































