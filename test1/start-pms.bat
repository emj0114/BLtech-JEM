@echo off
chcp 65001 >nul
title 나의 PMS  -  이 창을 닫으면 종료됩니다
cd /d "%~dp0"
echo.
echo   나의 PMS 를 시작하는 중입니다...
echo   잠시 후 브라우저가 자동으로 열립니다.
echo   ( 종료하려면 이 검은 창을 닫으세요 )
echo.
"C:\Users\emj01\AppData\Local\Programs\Python\Python312\python.exe" "%~dp0server.py" 8765
echo.
echo   PMS 서버가 종료되었습니다. 아무 키나 누르면 창이 닫힙니다.
pause >nul
