from flask import render_template
from flask import Flask
#from db import data
import sqlite3

app = Flask(__name__)


def get_patient():
    conn = sqlite3.connect('identifier.sqlite')

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `Patient`")
    results = cursor.fetchall()
    cursor.execute("SELECT * FROM `clinical_examination`")
    exam=cursor.fetchall()
    conn.close()
    return results,exam


data = get_patient()

print(data[0][0][2])


@app.route('/')
def main():
    dt=get_patient()
    return render_template('main.html',data=dt)


if __name__ == '__main__':
    app.run()
