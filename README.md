# flask-minijson
An extension for Flask to allow clients to submit data using the application/minijson codec

flask-json is required to be initialized before `FlaskMiniJSON`, in such a way:

```python
from flask_minijson import FlaskMiniJSON

app = Flask(__name__)
FlaskJSON(app)
FlaskMiniJSON(app)
```
