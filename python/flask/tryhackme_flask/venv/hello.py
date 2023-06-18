from flask import Flask, render_template,request
from werkzeug.utils import secure_filename

app = Flask(__name__)	# starts the flask project

def do_login():
	return 'This was a POST request!'
	
def show_login():
	return 'This was a GET request!'

@app.route('/')
def hello_world():
	return 'Hello, TryHackMe!'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return do_login()
	else:
		return show_login()

@app.route('/rendered')
def hello(name=None):
	return render_template('template.html', name=name)
	
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['the_file']
		f.save('/home/horus/Desktop/main/python/flask/tryhackme_flask/venv/uploads/' + secure_filename(f.filename))
	return render_template('upload.html')
