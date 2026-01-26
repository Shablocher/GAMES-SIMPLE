import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def init_db():
    with sqlite3.connect('space_war.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS ranking 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, pontos INTEGER, nivel TEXT)''')
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/save', methods=['POST'])
def save_score():
    data = request.json
    with sqlite3.connect('space_war.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ranking (nome, pontos, nivel) VALUES (?, ?, ?)',
                       (data['nome'], data['pontos'], data['nivel']))
        conn.commit()
    return jsonify({"status": "ok"})

@app.route('/api/ranking')
def get_ranking():
    with sqlite3.connect('space_war.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT nome, pontos, nivel FROM ranking ORDER BY pontos DESC LIMIT 5')
        return jsonify(cursor.fetchall())

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
