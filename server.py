from flask import Flask, render_template, url_for, request, redirect
import os, csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)

def write_to_csv(data):
	with open('database.csv',newline='', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		write_to_csv = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		write_to_csv.writerow([email,subject,message])



@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('thankyou.html')
		except:
			return 'Unable to send data.'
	else:
		return 'No i chuj, no i cześć'

