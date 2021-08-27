from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'marvin'
app.config['MYSQL_PASSWORD'] = 'marvin'
app.config['MYSQL_DB'] = 'postcomment_db'


mysql = MySQL(app)

cur = mysql.connect.cursor()
getData = "SELECT * FROM post_tbl"

@app.route('/')
def index():
    cur.execute(getData)
    mysql.connection.commit()
    cur.close()

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)