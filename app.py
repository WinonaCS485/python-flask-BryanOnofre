from flask import Flask, render_template
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='pi8643bb',
                             password='sailboat128',
                             db='pi8643bb_University',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# userInput = 'Kami'
userInput = input("Enter Name: ")
output = ''

try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = "SELECT * from Students WHERE fName =  " + "'" + userInput + "'"

        # execute the SQL command
        cursor.execute(sql)

        # get the results
        for result in cursor:
            output = result

        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes.
        # connection.commit()

finally:
    connection.close()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cakes')
def cakes():
    return render_template('cakes.html')


@app.route('/page')
def page():
    return render_template('page.html')


@app.route('/database')
def database():
    return render_template('database.html', output=output)


@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8643)
