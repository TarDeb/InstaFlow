# InstaFlow ELT Data - Instagram Auto Poster

This project automatically posts images to Instagram using Apache Airflow running in Docker containers.

## Prerequisites

1. **Docker Desktop** - Download and install from [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. **Instagram Account** - You'll need Instagram credentials

## Setup Instructions

### Step 1: Configure Instagram Credentials

Edit the `.env` file and add your Instagram credentials:
```
IG_USER=your_instagram_username
IG_PASS=your_instagram_password
```

### Step 2: Add Images

Place your images (JPG, PNG) in the `image/` directory.

### Step 3: Setup Airflow (First Time Only)

Run the setup script:
```bash
setup-airflow.bat
```

This will:
- Initialize the Airflow database
- Create necessary directories
- Set up the Docker environment

### Step 4: Start Airflow

```bash
start-airflow.bat
```

### Step 5: Access Airflow Web UI

Open your browser and go to: http://localhost:8080

- **Username:** airflow
- **Password:** airflow

### Step 6: Enable Your DAG

1. In the Airflow web UI, find the DAG named `test_instagram_post_every_5_minutes`
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

## Useful Commands

### Start Airflow
```bash
docker-compose up -d
```

### Stop Airflow
```bash
docker-compose down
```

### View Logs
```bash
docker-compose logs -f
```

### Restart Services
```bash
docker-compose restart
```

### View Running Containers
```bash
docker-compose ps
```

## Troubleshooting

### 1. Docker Issues
- Make sure Docker Desktop is running
- Check if ports 8080 and 5432 are available

### 2. Permission Issues
If you get permission errors, run:
```bash
docker-compose down
docker-compose up airflow-init
docker-compose up -d
```

### 3. Instagram Login Issues
- Make sure your Instagram credentials are correct
- Instagram may require 2FA - you might need an app password
- Check if your account has any restrictions

### 4. Image Issues
- Ensure images are in JPG or PNG format
- Check that the `image/` directory contains your photos
- Verify file permissions

## Configuration

### Change Posting Schedule

Edit `dags/weekly_post_dag.py` and modify the `schedule_interval`:

```python
# Post every hour
schedule_interval='0 * * * *'

# Post daily at 9 AM
schedule_interval='0 9 * * *'

# Post weekly on Mondays at 9 AM
schedule_interval='0 9 * * 1'
```

### Change Image Caption

Modify the caption in the `post_next_image()` function:

```python
post_image_instagram(image_path, caption=f"Your custom caption: {image_to_post}")
```

## Security Notes

- Never commit your `.env` file with real credentials
- Consider using Instagram app passwords instead of your main password
- Keep your Docker containers updated

## Support

If you encounter issues:
1. Check the Airflow logs in the web UI
2. Run `docker-compose logs -f` to see container logs
3. Ensure all prerequisites are installed correctly

Automate your Instagram: Automatically post an image from your folder to Instagram every week – powered by Python, Airflow & instagrapi.

---

## Features

- Automatically selects the next image from a folder
- Schedules weekly posting
- Uses Apache Airflow for workflow automation
- Secure Instagram login via environment variables or Airflow Connections
- Easily extendable (e.g., for other social media platforms)

## Requirements

- Python 3.8+
- [instagrapi](https://github.com/adw0rd/instagrapi)
- Apache Airflow
- An Instagram account (beware of Meta’s automation policies!)

## Installation

```bash
git clone https://github.com/your-username/InstaFlow.git
cd InstaFlow
pip install -r requirements.txt
