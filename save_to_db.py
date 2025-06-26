def save_result(url, mode, result, db_file, payload="", test_url="", status_code=None):
    import sqlite3
    import os

    os.makedirs(os.path.dirname(db_file), exist_ok=True)

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            mode TEXT,
            result TEXT,
            payload TEXT,
            test_url TEXT,
            status_code INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute(
        "INSERT INTO results (url, mode, result, payload, test_url, status_code) VALUES (?, ?, ?, ?, ?, ?)",
        (url, mode, result, payload, test_url, status_code)
    )
    conn.commit()
    conn.close()
        