# 웹 취약점 자동화 스캐너 (Gen-1)

웹 애플리케이션의 XSS(Cross-Site Scripting)와 SQL Injection 취약점을 자동으로 스캔하고 결과를 데이터베이스에 저장하는 도구입니다.

## 🚀 주요 기능

- **XSS 취약점 스캔**: 다양한 XSS 페이로드를 사용한 자동 테스트
- **SQL Injection 취약점 스캔**: SQL 인젝션 공격 패턴 탐지
- **GUI 인터페이스**: 사용자 친화적인 그래픽 인터페이스
- **CLI 인터페이스**: 명령줄에서 빠른 스캔 실행
- **결과 저장**: SQLite 데이터베이스에 스캔 결과 저장
- **CSV 내보내기**: 스캔 결과를 CSV 파일로 내보내기

## 📁 프로젝트 구조

```
Gen-1/
├── cli.py              # 명령줄 인터페이스
├── gui.py              # 그래픽 사용자 인터페이스
├── scanner_core.py     # 핵심 스캐너 로직
├── save_to_db.py       # 데이터베이스 저장 모듈
├── export_to_csv.py    # CSV 내보내기 모듈
├── Database/           # 데이터베이스 파일 저장소
│   └── scanner_results.db
├── CSV/                # CSV 파일 저장소
│   └── scan_results.csv
├── LICENSE             # MIT 라이선스
└── README.md
```

## 🛠️ 설치 및 실행

### 필수 요구사항

- Python 3.6 이상
- `requests` 라이브러리

### 설치

```bash
# requests 라이브러리 설치
pip install requests
```

### 실행 방법

#### 1. GUI 모드 (권장)

```bash
python gui.py
```

GUI에서 다음을 설정할 수 있습니다:
- 대상 URL 입력
- 스캔 모드 선택 (XSS, SQL Injection, All)
- CSV 내보내기 옵션

#### 2. CLI 모드

```bash
# XSS 스캔
python cli.py --url "http://example.com" --mode xss

# SQL Injection 스캔
python cli.py --url "http://example.com" --mode sqli

# 모든 취약점 스캔
python cli.py --url "http://example.com" --mode all

# 결과를 CSV로 내보내기
python cli.py --url "http://example.com" --mode all --export
```

## 🔍 스캔 기능

### XSS 스캔
다음과 같은 페이로드를 사용하여 XSS 취약점을 탐지합니다:
- `<script>alert(1)</script>`
- `"><script>alert(1)</script>`
- `'><img src=x onerror=alert(1)>`

### SQL Injection 스캔
다음과 같은 페이로드를 사용하여 SQL Injection 취약점을 탐지합니다:
- `' OR '1'='1`
- `' OR 1=1 -- `
- `'; DROP TABLE users -- `
- `" OR "" = ""`

## 📊 결과 저장

### 데이터베이스 구조
스캔 결과는 SQLite 데이터베이스에 다음 정보와 함께 저장됩니다:
- URL
- 스캔 모드 (xss/sqli)
- 결과 (취약/안전/요청실패)
- 사용된 페이로드
- 테스트 URL
- HTTP 상태 코드
- 타임스탬프

### CSV 내보내기
데이터베이스의 모든 결과를 CSV 파일로 내보낼 수 있습니다.

## ⚠️ 주의사항

- **법적 책임**: 이 도구는 교육 및 보안 테스트 목적으로만 사용하세요.
- **권한**: 테스트 대상 웹사이트에 대한 적절한 권한을 확보하세요.
- **책임**: 무단 테스트로 인한 법적 문제는 사용자에게 있습니다.

## 🐛 문제 해결

### 일반적인 문제

1. **requests 모듈 오류**
   ```bash
   pip install requests
   ```

2. **데이터베이스 접근 오류**
   - Database 폴더가 존재하는지 확인
   - 파일 권한 확인

3. **CSV 내보내기 실패**
   - CSV 폴더가 존재하는지 확인
   - 파일 쓰기 권한 확인

## 📝 라이선스

이 프로젝트는 [MIT 라이선스](LICENSE) 하에 배포됩니다.

**주요 라이선스 조건:**
- 자유로운 사용, 수정, 배포 가능
- 상업적 사용 가능
- 원본 저작권 표시 필요
- 저작자는 책임을 지지 않음

**중요한 면책 조항:**
이 소프트웨어는 교육 및 보안 테스트 목적으로만 제공됩니다. 저작자는 이 소프트웨어의 오용에 대해 책임지지 않습니다. 사용자는 테스트하려는 시스템에 대한 적절한 권한을 확보해야 하며, 무단 테스트는 불법일 수 있고 법적 결과를 초래할 수 있습니다.

## 🤝 기여

버그 리포트나 기능 제안은 이슈로 등록해 주세요.

---

**⚠️ 경고**: 이 도구는 보안 테스트 목적으로만 사용하시고, 적절한 권한 없이 타인의 시스템을 테스트하지 마세요. 
