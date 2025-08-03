"""
Enhanced Instagram Poster with Better Authentication
Handles common Instagram login issues
"""
import os
import sys
import time
from datetime import datetime

# Add scripts to path
sys.path.append('scripts')

def enhanced_instagram_login():
    """Enhanced login with better error handling"""
    from dotenv import load_dotenv
    from instagrapi import Client
    
    load_dotenv()
    
    username = os.environ.get("IG_USER")
    password = os.environ.get("IG_PASS")
    
    if not username or not password:
        print("❌ Credentials not found in .env file")
        return None
    
    print(f"🔐 Attempting login for: {username}")
    
    # Create client with enhanced settings
    cl = Client()
    
    # Set user agent to avoid bot detection
    cl.set_user_agent("Instagram 219.0.0.12.117 Android")
    
    try:
        # Method 1: Try standard login
        print("📱 Trying standard login...")
        cl.login(username, password)
        print("✅ Login successful!")
        return cl
        
    except Exception as e:
        error_msg = str(e).lower()
        
        if "challenge" in error_msg or "verification" in error_msg:
            print("⚠️  Instagram requires verification")
            print("Solutions:")
            print("1. Login to Instagram on your browser first")
            print("2. Verify your account via email/SMS")
            print("3. Wait 24-48 hours and try again")
            
        elif "rate" in error_msg or "blocked" in error_msg:
            print("⚠️  Rate limited or IP blocked")
            print("Solutions:")
            print("1. Wait several hours before trying again")
            print("2. Use VPN to change IP address")
            print("3. Login to Instagram normally first")
            
        elif "password" in error_msg or "login" in error_msg:
            print("⚠️  Login credentials issue")
            print("Solutions:")
            print("1. Check username/password are correct")
            print("2. Use username instead of email")
            print("3. Disable 2FA temporarily")
            
        else:
            print(f"⚠️  Other error: {e}")
        
        return None

def post_with_enhanced_auth():
    """Post image with enhanced authentication"""
    
    print("🔐 ENHANCED INSTAGRAM AUTHENTICATION")
    print("=" * 50)
    
    # Get Instagram client
    cl = enhanced_instagram_login()
    
    if not cl:
        print("❌ Could not authenticate with Instagram")
        return False
    
    # Check images
    IMAGES_DIR = 'image'
    COUNTER_FILE = 'counter.txt'
    
    images = sorted([f for f in os.listdir(IMAGES_DIR) 
                    if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    
    if not images:
        print("❌ No images found!")
        return False
    
    # Get current image
    idx = 0
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'r') as f:
            content = f.read().strip()
            idx = int(content) if content else 0
    
    image_to_post = images[idx % len(images)]
    image_path = os.path.join(IMAGES_DIR, image_to_post)
    caption = f"Auto post: {image_to_post}"
    
    try:
        print(f"\n📸 Posting: {image_to_post}")
        print(f"📝 Caption: {caption}")
        print("⏰ Uploading...")
        
        # Upload photo
        cl.photo_upload(image_path, caption)
        
        print("✅ SUCCESS! Image posted to Instagram!")
        
        # Update counter
        new_idx = (idx + 1) % len(images)
        with open(COUNTER_FILE, 'w') as f:
            f.write(str(new_idx))
        
        print(f"🔄 Counter updated: {idx} → {new_idx}")
        
        return True
        
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        return False

if __name__ == "__main__":
    print("📱 Enhanced Instagram Poster")
    
    success = post_with_enhanced_auth()
    
    if success:
        print("\n🎉 Image successfully posted to Instagram!")
        print("Check your Instagram account to see the post")
    else:
        print("\n❌ Posting failed")
        print("\n🔧 Troubleshooting steps:")
        print("1. Login to Instagram on web browser first")
        print("2. Make sure account is not restricted")
        print("3. Try using Instagram username instead of email")
        print("4. Disable 2FA temporarily")
        print("5. Wait and try again later")
    
    input("\nPress Enter to exit...")
