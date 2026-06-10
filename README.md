# BLtech-JEM

개인 개발 환경 및 업무 관리(PMS) 작업 공간.

## 구성

### 나의 PMS (개인 업무 관리 웹앱)
회사 업무 / 오늘 꼭 할 일 / 개인 업무 / 자기계발 / 개인 일정을 카테고리별로 관리하는 가벼운 칸반형 웹앱.
앱 파일은 저장소 최상위에 있으며, Vercel 등 정적 호스팅에 그대로 배포됩니다(루트 `index.html`).

- `index.html` — 앱 본체 (우선순위·마감일·메모·진행률 대시보드·JSON 백업)
- `server.py` — 데이터를 `data.json` 파일에 저장하는 로컬 서버 (표준 라이브러리만 사용)
- `start-pms.bat` — 더블클릭하면 서버 실행 + 브라우저 자동 오픈

**로컬 실행:** `start-pms.bat` 더블클릭 (또는 `python server.py`). 데이터는 `data.json` 에 자동 저장됩니다(저장소에는 올리지 않음).
**배포(웹):** 정적 호스팅에서는 로컬 서버가 없으므로 브라우저 localStorage 에 자동 저장됩니다.

## 개발 환경
- Node.js / TypeScript (`package.json`, `tsconfig.json`)
- Python 3.12 + 가상환경 `.venv` (openpyxl, pandas, xlsxwriter, playwright)

### 설치 (새 PC에서 받았을 때)
```powershell
npm install          # Node 의존성
python -m venv .venv
.\.venv\Scripts\pip install openpyxl pandas xlsxwriter playwright
```
