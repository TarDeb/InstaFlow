# InstaFlow - Instagram Auto Poster

This project automatically posts images to Instagram using Apache Airflow running in Docker containers.

## Prerequisites

1. **Docker Desktop** - 
2. **Instagram Account** - Instagram credentials
## Setup Instructions
### Step 1: Configure Instagram Credentials
Edit the `.env` file and add your Instagram credentials:
```
IG_USER=your_instagram_username
IG_PASS=your_instagram_password
```
### Step 2: Add Images
Place  images (JPG, PNG) in the `image/` directory.
### Step 3: Setup Airflow 
- Initialize the Airflow database
- Create necessary directories
- Set up the Docker environment
### Step 5: Access Airflow
Open-> http://localhost:8080
- **Username:** airflow
- **Password:** airflow

### Step 6: Enable DAG

1. In the Airflow web UI, find the DAG named
2. Click the toggle switch to enable it
3. The DAG will start posting images every 5 minutes

## Project Structure

```
InstaFlow_ELT_data/
├── dags/                          # Airflow DAGs
│   └── weekly_post_dag.py        # Main Instagram posting DAG
├── scripts/                       # Python scripts
│   └── post_image.py             # Instagram posting logic
├── image/                         # Images to post
│   ├── DJI_0120.JPG
│   ├── DJI_0124.JPG
│   └── DJI_0125.JPG
├── logs/                          # Airflow logs
├── plugins/                       # Airflow plugins
├── .env                          # Instagram credentials
├── counter.txt                   # Image rotation counter
├── docker-compose.yml           # Docker configuration
└── README.md                     # This file
```
## Features
- Automatically selects the next image from a folder
- Schedules weekly posting
- Uses Apache Airflow for workflow automation
- Secure Instagram login via environment variables or Airflow Connections
- Easily extendable (e.g., for other social media platforms)



