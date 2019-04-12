from flask import Flask, render_template
import pymysql # This librsry provides functionaslity to access mysql.

app = Flask(__name__)

@app.route("/search/lastName")
def lastName():
    return render_template("lastName.html")
    
@app.route("/search/location")
def location():
    return render_template("location.html")
    
@app.route("/search/id")
def globalSearch():
    return render_template("id.html")

@app.route("/")
def main():
    #return render_template('index.html')
    print("Here in main")
    return render_template("start.html")

class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "bisvseniorproject"
        db = "Police_Records"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def list_records(self):
        self.cur.execute("SELECT * FROM Police_Records.police_data LIMIT 50")
        result = self.cur.fetchall()

        return result

@app.route('/fetch_police_records')
def fetch_police_records():

    def db_query():
        db = Database()
        records = db.list_records()

        return records

    res = db_query()

    return render_template('police_records.html', result=res, content_type='application/json')

if __name__ == "__main__":
    app.run()
