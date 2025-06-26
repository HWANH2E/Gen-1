def export_to_csv(db_file, csv_file):
    import sqlite3
    import csv
    import os

    os.makedirs(os.path.dirname(csv_file), exist_ok=True)

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT url, mode, result, payload, test_url, status_code, timestamp FROM results")
    rows = cursor.fetchall()

    if not rows:
        print("[!] 저장된 결과가 없습니다.")
        return

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["url", "mode", "result", "payload", "test_url", "status_code", "timestamp"])
        writer.writerows(rows)

    conn.close()
    print(f"[✓] 결과가 CSV로 저장됨: {csv_file}")
