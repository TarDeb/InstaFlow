@echo off
echo Starting Airflow services...

REM Start all Airflow services
docker-compose up -d

echo.
echo Airflow is starting up...
echo.
echo Web UI will be available at: http://localhost:8080
echo Username: airflow
echo Password: airflow
echo.
echo To stop Airflow, run: docker-compose down
echo To view logs, run: docker-compose logs -f
echo.
pause
