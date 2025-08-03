@echo off
echo Setting up Airflow with Docker...

REM Check if Docker is installed
docker --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ERROR: Docker is not installed or not in PATH
    echo Please install Docker Desktop from: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

echo Docker found! Proceeding with setup...

REM Copy environment file
copy .env.docker .env

REM Initialize Airflow database
echo Initializing Airflow database...
docker-compose up airflow-init

echo.
echo Setup complete! You can now start Airflow with:
echo   docker-compose up
echo.
echo Airflow will be available at: http://localhost:8080
echo Username: airflow
echo Password: airflow
echo.
pause
