import argparse
from scanner_core import scan_xss, scan_sqli
from export_to_csv import export_to_csv

# 기본 경로
DEFAULT_DB_PATH = r"C:\Users\hwanh\Desktop\Gen-1(test)\Database\scanner_results.db"
DEFAULT_CSV_PATH = r"C:\Users\hwanh\Desktop\Gen-1(test)\CSV\scan_results.csv"

# argparse 설정 (한 번만)
parser = argparse.ArgumentParser(description="웹 취약점 자동화 스캐너")
parser.add_argument("--url", required=True, help="대상 URL")
parser.add_argument("--mode", choices=["xss", "sqli", "all"], required=True)
parser.add_argument("--export", action="store_true")
parser.add_argument("--db", default=DEFAULT_DB_PATH)
parser.add_argument("--csv", default=DEFAULT_CSV_PATH)

args = parser.parse_args()

if args.mode == "xss":
    scan_xss(args.url, args.db)
elif args.mode == "sqli":
    scan_sqli(args.url, args.db)
elif args.mode == "all":
    scan_xss(args.url, args.db)
    scan_sqli(args.url, args.db)
    
if args.export:
    export_to_csv(args.db, args.csv)