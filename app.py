from flask import Flask
from flask import request
from toneanalysis import gettone
import json

app = Flask(__name__)

@app.route('/status')
def status():
    return 'RUNNING'

@app.route('/analyze', methods=['GET', 'POST'])
def tone():
    if request.method == 'POST':
        jsonresp = request.get_json()
        resp = json.loads(jsonresp)
        print resp.get("text")
        text= resp.get("text")
    else:
        text = request.values.get("text")
    print text
    response = app.response_class(
        response=gettone(text),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')