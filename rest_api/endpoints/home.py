from rest_api.app import app
from flask_login import login_required

@app.route('/')
@login_required
def hello_world():
    return 'Hello, World!'

