import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, logging
import pymysql # This library provides functionality to access mysql.
app = Flask(__name__)

class Database:
	def __init__(self):
		host = "127.0.0.1"
		user = "root"
		password = "bisvseniorproject"
		db = "POLICE_RECORDS"
		self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
								   DictCursor)
		self.cur = self.con.cursor()

	def listAllrecords(self):
		self.cur.execute("SELECT * FROM Police_Records.police_data LIMIT 50")
		result = self.cur.fetchall()
		return result

	def listRecordById(self, officerId):
		sqlQuery = "SELECT * FROM Police_Records.police_data where officer_id = \'" + officerId + "\';"
		self.cur.execute(sqlQuery)
		result = self.cur.fetchall()
		return result

	def listRecordByLastName(self, officerLastName):
		sqlQuery = "SELECT * FROM Police_Records.police_data where officer_last_name = \'" + officerLastName + "\';"
		self.cur.execute(sqlQuery)
		result = self.cur.fetchall()
		return result

	def listRecordByLocation(self, location):
		sqlQuery = "SELECT * FROM Police_Records.police_data where officer_state = \'" + location + "\';"
		self.cur.execute(sqlQuery)
		result = self.cur.fetchall()
		return result
		
	def authenticate(self, user, password):
		try:
			db = "Police_Records"
			self.con = pymysql.connect(host='127.0.0.1', user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
		except Exception as e:
			print ("SQL connect error" % e)
			return False
		return True


@app.route("/search/lastName", methods=['POST', 'GET'])
def searchLastName():
	if request.method == 'GET':
		return render_template("lastName.html")
	dict = request.form
	for key in dict:
		print ('form key %s' % dict[key])
	lastName = request.form['lastName']
	db = Database()
	res = db.listRecordByLastName(lastName)	
	return render_template('police_records.html', result=res, content_type='application/json')
	
@app.route("/search/map", methods=['GET'])
def searchMap():
	if request.method == 'GET':
		return render_template("map.html")
	dict = request.form
	for key in dict:
		print ('form key %s' % dict[key])
	location = request.form['state']
	db = Database()
	res = db.listRecordByLocation(location)
	return render_template('police_records.html', result=res, content_type='application/json')

@app.route("/search/location", methods=['GET'])
def searchLocation():
	if 'state' not in request.args:
		return home() #error
	location = request.args.get("state", "")
	print ("location is %s" % location)
	db = Database()
	res = db.listRecordByLocation(location)
	return render_template('police_records.html', result=res, content_type='application/json')
	
	
@app.route("/search/id", methods=['POST', 'GET'])
def searchId():
	if request.method == 'GET':
		return render_template("id.html")
	offId = request.form['id1']
	#print("officer id is %s" % offId)
	db = Database()
	res = db.listRecordById(offId)
	return render_template('police_records.html', result=res, content_type='application/json')
	
@app.route("/login", methods=['POST'])
def login():
	user = request.form['username']
	passw = request.form['password']

	db = Database()
	if db.authenticate(user, passw) is True:
		session['logged_in'] = True
		flash('You were successfully logged in')
		return render_template("updateDatabase.html")
	else:
		flash('wrong password!')
		return home()

@app.route("/updateDatabase", methods=['POST', 'GET'])
def updateDb():
	if request.method == 'GET':
		if not session.get('logged_in'):
			return render_template('login.html')
		else:
			return render_template("updateDatabase.html")

@app.route('/fetch_police_records')
def fetch_police_record():

    def db_query():
        db = Database()
        records = db.listAllrecords()
        return records

    res = db_query()

    return render_template('police_records.html', result=res, content_type='application/json')

@app.route("/")
def home():
	return render_template("start.html")
	
def main():
    return home()
	
if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run()


