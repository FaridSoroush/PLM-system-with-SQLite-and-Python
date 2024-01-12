from flask import Flask, jsonify, request
import sqlite3

conn = sqlite3.connect('pcb_plm.db')
print(conn.execute('SELECT * FROM pcb_designs').fetchall())
conn.close()
