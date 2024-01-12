from flask import Flask, jsonify, request
import sqlite3

"Setting up the root path:"

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('pcb_plm.db')
    conn.row_factory = sqlite3.Row  # This makes the rows dictionary-like
    return conn

@app.route('/')
def index():
    return "Welcome to the PCB Design PLM API!"


"""
Add Endpoints for PCB Designs
Add endpoints to perform CRUD operations on PCB designs. 
Here's an example for retrieving all PCB designs:
"""

@app.route('/pcb_designs', methods=['GET'])
def get_pcb_designs():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pcb_designs')
        designs = cursor.fetchall()
        conn.close()
        return jsonify([dict(row) for row in designs])
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


"""
Add Endpoints for Issues
Similarly, add endpoints for managing issues:
"""

@app.route('/issues', methods=['GET'])
def get_issues():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pcb_issues')
        issues = cursor.fetchall()
        conn.close()
        return jsonify([dict(row) for row in issues])
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Change the port number

