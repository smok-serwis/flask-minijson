from flask import Flask, request
from flask_json import FlaskJSON, as_json
from flask_minijson import FlaskMiniJSON

app = Flask(__name__)
FlaskJSON(app)
FlaskMiniJSON(app)

app.config['DEBUG'] = True
app.config['TESTING'] = True


@app.route('/v1', methods=['POST'])
@as_json
def example_point():
    if request.get_json() == {'1': '2'}:
        return {'status': 'ok'},
    else:
        return {'status': 'fail'}
