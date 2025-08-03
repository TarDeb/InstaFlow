"""
Standalone Instagram poster script that works on Windows
This script replaces the Airflow DAG for testing purposes
"""
import os
import sys
import time
import schedule
from datetime import datetime

# Add the 'scripts' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'scripts')))
from post_image import post_image_instagram

# Paths to your images and the counter file
IMAGES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'image'))
COUNTER_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'counter.txt'))

def post_next_image():
    """Post the next image in rotation"""
    try:
        images = sorted([f for f in os.listdir(IMAGES_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
        if not images:
            raise ValueError("No images found in the folder!")
        
        # Read current counter
        idx = 0
        if os.path.exists(COUNTER_FILE):
            with open(COUNTER_FILE, 'r') as f:
                content = f.read().strip()
                idx = int(content) if content else 0
        
        # Get image to post
        image_to_post = images[idx % len(images)]
        image_path = os.path.join(IMAGES_DIR, image_to_post)
        
        print(f"[{datetime.now()}] Posting image: {image_to_post}")
        post_image_instagram(image_path, caption=f"Auto post: {image_to_post}")
        print(f"[{datetime.now()}] Successfully posted {image_to_post}")
        
        # Update counter
        with open(COUNTER_FILE, 'w') as f:
            f.write(str((idx + 1) % len(images)))
        
    except Exception as e:
        print(f"[{datetime.now()}] Error posting image: {str(e)}")
        raise

def run_scheduler():
    """Run the scheduler for posting images"""
    print(f"[{datetime.now()}] 🚀 Instagram Auto Poster Started!")
    print(f"📁 Images directory: {IMAGES_DIR}")
    print(f"📄 Counter file: {COUNTER_FILE}")
    
    # Schedule to run every 2 minutes
    schedule.every(2).minutes.do(post_next_image)
    
    # Post first image immediately
    print(f"[{datetime.now()}] 📸 Posting first image now...")
    try:
        post_next_image()
    except Exception as e:
        print(f"❌ First post failed: {e}")
    
    print(f"[{datetime.now()}] ⏰ Scheduler active. Next post in 2 minutes.")
    print("Press Ctrl+C to stop...")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()
