import tkinter as tk
from tkinter import messagebox
from scanner_core import scan_xss, scan_sqli
from export_to_csv import export_to_csv


# 기본 경로
DB_PATH = r"C:\Users\hwanh\Desktop\Gen-1(test)\Database\scanner_results.db"
CSV_PATH = r"C:\Users\hwanh\Desktop\Gen-1(test)\CSV\scan_results.csv"

def run_scan():
    url = entry_url.get()
    mode = scan_mode.get()
    export = export_var.get()
    
    if not url:
        messagebox.showerror("경고", "URL을 입력하세요.")
        return
    
    if mode == "xss":
        scan_xss(url, db_file=DB_PATH)
        
    elif mode == "sqli":
        scan_sqli(url, db_file=DB_PATH)
    
    elif mode == "all":
        scan_xss(url, db_file=DB_PATH)
        scan_sqli(url, db_file=DB_PATH)
        
    if export:
        export_to_csv(DB_PATH, CSV_PATH)
        
    messagebox.showinfo("완료", "스캔이 완료되었습니다.")
    
# GUI 만들기
root = tk.Tk()
root.title("웹 취약점 스캐너")
root.geometry("400x300")

# URL 입력
tk.Label(root, text="대상 URL:").pack(pady=5)
entry_url = tk.Entry(root, width=50)
entry_url.pack()

tk.Label(root, text="⚙ 스캔 모드 선택:").pack(pady=5)
scan_mode = tk.StringVar(value="xss")
tk.Radiobutton(root, text="XSS", variable=scan_mode, value="xss").pack()
tk.Radiobutton(root, text="SQL Injection", variable=scan_mode, value="sqli").pack()
tk.Radiobutton(root, text="All", variable=scan_mode, value="all").pack()

# 결과 CSV 저장 옵션
export_var = tk.BooleanVar()
tk.Checkbutton(root, text="결과를 CSV로 저장", variable=export_var).pack(pady=10)

# 스캔 실행 버튼
tk.Button(root, text="스캔 실행", command=run_scan, bg="green", fg="white").pack(pady=15)

root.mainloop()    