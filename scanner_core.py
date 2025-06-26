from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from save_to_db import save_result
import requests

# 기본 경로 상수
DEFAULT_DB_PATH = r"C:\Users\hwanh\Desktop\Gen-1(test)\Database\scanner_results.db"
DEFAULT_CSV_PATH = r"C:\Users\hwanh\Desktop\Gen-1(test)\CSV\scan_results.csv"


def scan_xss(target_url, db_file):
    print(f"[+] XSS 스캔 실행 중: {target_url}")
    payloads = [
        "<script>alert(1)</script>",
        "\"><script>alert(1)</script>",
        "'><img src=x onerror=alert(1)>",
    ]

    parsed = urlparse(target_url)
    query = parse_qs(parsed.query)

    for payload in payloads:
        temp_query = query.copy()

        if not temp_query:
            temp_query["input"] = [payload]  # 기본 파라미터 이름
        else:
            for key in temp_query:
                temp_query[key] = [payload]

        encoded_query = urlencode(temp_query, doseq=True)
        test_url = urlunparse(parsed._replace(query=encoded_query))

        print(f"[+] 테스트 URL: {test_url}")

        try:
            response = requests.get(test_url, timeout=5)
            if payload in response.text:
                print(f"[!] XSS 취약점 발견! {test_url}")
                save_result(target_url, "xss", "취약", db_file, payload, test_url, response.status_code)    
                return
        except Exception as e:
            print(f"[X] 요청 실패 {e}")
            save_result(target_url, "xss", "요청실패", db_file, payload, test_url, -1)
            return

    print("[✓] XSS 취약점 없음")
    save_result(target_url, "xss", "안전", db_file, "", "", 200)


def scan_sqli(target_url, db_file):
    print(f"[+] SQL Injection 스캔 실행 중: {target_url}")

    payloads = [
        "' OR '1'='1",
        "' OR 1=1 -- ",
        "'; DROP TABLE users -- ",
        "\" OR \"\" = \"",
    ]

    error_keywords = [
        "SQL syntax", "mysql_fetch", "ORA-", "You have an error in your SQL",
        "Warning: SQL Injection", "unterminated quoted string"
    ]

    parsed = urlparse(target_url)
    query = parse_qs(parsed.query)

    for payload in payloads:
        temp_query = query.copy()

        if not temp_query:
            temp_query["id"] = [payload]  # 기본 파라미터 이름
        else:
            for key in temp_query:
                temp_query[key] = [payload]

        encoded_query = urlencode(temp_query, doseq=True)
        test_url = urlunparse(parsed._replace(query=encoded_query))

        try:
            response = requests.get(test_url, timeout=5)

            if any(error in response.text for error in error_keywords):
                print(f"[!] SQL Injection 취약점 발견!: {test_url}")
                save_result(target_url, "sqli", "취약", db_file, payload, test_url, response.status_code)
                return

        except Exception as e:
            print(f"[X] 요청 실패: {e}")
            save_result(target_url, "sqli", "요청실패", db_file, payload, test_url, -1)
            return

    print("[✓] SQL Injection 취약점 없음 (안전)")
    save_result(target_url, "sqli", "안전", db_file, "", "", 200)