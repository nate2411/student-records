import sqlite3

from flask import Flask, render_template, request, jsonify


def init_sqlite_db():


    conn = sqlite3.connect("database.db")
    print("OPened database successfully")


    conn.execute("CREATE TABLE IF NOT EXISTS  students (name TEXT, addr TEXT, city TEXT, pin TEXT)")
    print("Table created successfully")
    conn.close()


init_sqlite_db()
app = Flask(__name__)

@app.route('/add-new-record/', methods=["POST"])
def add_new_student_record():
    msg = None

    if request.method == "POST":
        try:
            name = request.form['name']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                return render_template('result.html', msg=msg)
@app.route('/show-students-data/')
def show_student_data():

    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")


        results = cur.fetchall()

        return jsonify(results)
     
    if __name__ == '__main__':
        app.debug = True
        app.run()
