from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def employee_list() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'employee'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM employee_list')
    results = [{firstname: lastname} for (firstname, lastname) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'employee_list': employee_list()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
