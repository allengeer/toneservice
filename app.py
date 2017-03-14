from flask import Flask
from flask import request
from toneanalysis import gettone

app = Flask(__name__)

@app.route('/status')
def status():
    return 'RUNNING'

@app.route('/analyze', methods=['GET', 'POST'])
def tone():
    text = request.values.get("text")
    response = app.response_class(
        response=gettone(text),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5005)