@echo off
echo Starting FastAPI with Uvicorn...
python -m uvicorn app.main:app --host 0.0.0.0 --port 10000
pause
