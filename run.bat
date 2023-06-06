@REM uvicorn main:app --reload

gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app