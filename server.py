from flask import Flask, request, render_template, redirect, session, flash  # Import Flask to allow us to create our app.
from mysqlconnection import MySQLConnector
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
def index(): 
  query = "SELECT name, age, date_format(created_at, '%M %d') as date1, date_format(created_at, '%Y') as date2 FROM friends"

  friend_list = mysql.query_db(query)
  return render_template('index.html', friends = friend_list)  # Return 'Hello World!' to the response.

@app.route('/submit', methods=['POST'])
def submit():
	name = request.form['name']
	age = request.form['age']
	query = "INSERT into friends (name, age, created_at, updated_at) values (:name, :age ,now(), now())"
	data = {'name':name, 'age':age}
	mysql.query_db(query, data)
	return redirect('/')
app.run(debug=True)