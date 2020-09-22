from flask import Flask
from datetime import datetime
import time
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def show_time():

	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")    
	return ("Current time is "+ current_time)

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
