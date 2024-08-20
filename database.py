import sqlite3

def init_db():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bmi_records
                 (id INTEGER PRIMARY KEY, weight REAL, height REAL, bmi REAL, category TEXT, date TEXT)''')
    conn.commit()
    conn.close()

def save_record(weight, height, bmi, category):
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO bmi_records (weight, height, bmi, category, date) VALUES (?, ?, ?, ?, datetime('now'))",
              (weight, height, bmi, category))
    conn.commit()
    conn.close()

def get_records():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bmi_records")
    records = c.fetchall()
    conn.close()
    return records

init_db()
