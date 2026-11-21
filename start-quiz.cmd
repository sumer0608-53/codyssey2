@echo off
setlocal
cd /d "%~dp0"
chcp 65001 >nul
where py >nul 2>nul
if errorlevel 1 goto python
py -3 -c "import sys; sys.exit(sys.version_info < (3, 10))" >nul 2>nul
if errorlevel 1 goto python
py -3 -X utf8 main.py
set "result=%errorlevel%"
goto done
:python
where python >nul 2>nul
if errorlevel 1 goto missing
python -c "import sys; sys.exit(sys.version_info < (3, 10))" >nul 2>nul
if errorlevel 1 goto missing
python -X utf8 main.py
set "result=%errorlevel%"
goto done
:missing
echo Python 3.10 or newer is required.
set "result=1"
:done
pause
exit /b %result%
