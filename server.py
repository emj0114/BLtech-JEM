# -*- coding: utf-8 -*-
"""나의 PMS - 로컬 저장 서버
데이터를 같은 폴더의 data.json 파일에 저장한다. 외부 의존성 없음(표준 라이브러리만 사용).
사용법:  python server.py [포트]   (기본 포트 8765)
"""
import http.server
import socketserver
import json
import os
import sys
import threading
import webbrowser

PORT = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 8765
BASE = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE)
DATA = os.path.join(BASE, "data.json")


class Handler(http.server.SimpleHTTPRequestHandler):
    def _json(self, code, body_bytes):
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body_bytes)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body_bytes)

    def do_GET(self):
        if self.path.split("?")[0] == "/api/data":
            try:
                with open(DATA, "r", encoding="utf-8") as f:
                    body = f.read()
            except FileNotFoundError:
                body = "[]"
            return self._json(200, body.encode("utf-8"))
        return super().do_GET()

    def do_POST(self):
        if self.path.split("?")[0] != "/api/data":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        try:
            data = json.loads(raw.decode("utf-8"))
            tmp = DATA + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            os.replace(tmp, DATA)  # 원자적 저장 (저장 중 깨짐 방지)
            return self._json(200, b'{"ok":true}')
        except Exception as e:
            return self._json(500, json.dumps({"ok": False, "error": str(e)}).encode("utf-8"))

    def log_message(self, *args):
        pass  # 콘솔 깔끔하게


def main():
    http.server.ThreadingHTTPServer.allow_reuse_address = True
    try:
        httpd = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    except OSError as e:
        print(f"[오류] 포트 {PORT} 를 사용할 수 없습니다. 이미 PMS가 켜져 있는지 확인하세요.\n{e}")
        return
    url = f"http://localhost:{PORT}/"
    print("=" * 52)
    print("  나의 PMS 가 실행되었습니다.")
    print(f"  주소     : {url}")
    print(f"  저장 파일 : {DATA}")
    print("  ※ 이 검은 창을 닫으면 PMS가 종료됩니다. 계속 켜두세요.")
    print("=" * 52)
    if "--no-browser" not in sys.argv:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
