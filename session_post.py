"""
Instagram Poster with Session Management
Saves login session to avoid repeated authentication
"""
import os
import sys
import json
from datetime import datetime

# Add scripts to path
sys.path.append('scripts')

def login_with_session():
    """Login using saved session or create new one"""
    from dotenv import load_dotenv
    from instagrapi import Client
    
    load_dotenv()
    
    username = os.environ.get("IG_USER")
    password = os.environ.get("IG_PASS")
    session_file = "instagram_session.json"
    
    if not username or not password:
        print("❌ Credentials not found")
        return None
    
    print(f"🔐 Authenticating: {username}")
    
    cl = Client()
    
    # Try to load existing session
    if os.path.exists(session_file):
        print("📁 Found existing session, trying to load...")
        try:
            cl.load_settings(session_file)
            cl.login(username, password)
            print("✅ Session loaded successfully!")
            return cl
        except Exception as e:
            print(f"⚠️  Session invalid: {e}")
            print("🔄 Creating new session...")
    
    # Create new session
    try:
        print("🆕 Creating new session...")
        
        # Try different methods
        methods = [
            lambda: cl.login(username, password),
        ]
        
        for i, method in enumerate(methods, 1):
            try:
                print(f"   Method {i}: Attempting login...")
                method()
                print("✅ Login successful!")
                
                # Save session
                cl.dump_settings(session_file)
                print(f"💾 Session saved to {session_file}")
                
                return cl
                
            except Exception as e:
                print(f"   ❌ Method {i} failed: {e}")
                continue
        
        print("❌ All login methods failed")
        return None
        
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        return None

def safe_post_image():
    """Safely post image with session management"""
    
    print("📱 SESSION-BASED INSTAGRAM POSTER")
    print("=" * 50)
    
    # Authenticate
    cl = login_with_session()
    if not cl:
        print("\n❌ Could not authenticate")
        print("\n💡 Try these solutions:")
        print("1. Use your Instagram username (not email) in .env")
        print("2. Login to Instagram on browser first")
        print("3. Check if account has 2FA enabled")
        print("4. Wait 30 minutes and try again")
        return False
    
    # Get images
    IMAGES_DIR = 'image'
    COUNTER_FILE = 'counter.txt'
    
    try:
        images = sorted([f for f in os.listdir(IMAGES_DIR) 
                        if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
        
        if not images:
            print("❌ No images found in 'image' directory")
            return False
        
        # Get current image
        idx = 0
        if os.path.exists(COUNTER_FILE):
            with open(COUNTER_FILE, 'r') as f:
                content = f.read().strip()
                idx = int(content) if content else 0
        
        image_to_post = images[idx % len(images)]
        image_path = os.path.join(IMAGES_DIR, image_to_post)
        
        print(f"\n📸 Posting image: {image_to_post}")
        print(f"📁 Path: {image_path}")
        
        # Check if file exists
        if not os.path.exists(image_path):
            print(f"❌ Image file not found: {image_path}")
            return False
        
        # Post image
        caption = f"Auto post: {image_to_post} 📸 #automation #instagram"
        
        print("📤 Uploading to Instagram...")
        result = cl.photo_upload(image_path, caption)
        
        if result:
            print("🎉 SUCCESS! Image posted to Instagram!")
            print(f"📊 Post ID: {result.id}")
            
            # Update counter
            new_idx = (idx + 1) % len(images)
            with open(COUNTER_FILE, 'w') as f:
                f.write(str(new_idx))
            
            print(f"🔄 Counter: {idx} → {new_idx}")
            print(f"📅 Next image: {images[new_idx]}")
            
            return True
        else:
            print("❌ Upload failed - no result returned")
            return False
            
    except Exception as e:
        print(f"❌ Error during posting: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Instagram Auto Poster with Session Management")
    print("This version saves login sessions to avoid repeated authentication")
    print()
    
    success = safe_post_image()
    
    if success:
        print("\n✅ Image successfully posted!")
        print("🔗 Check your Instagram to see the post")
        print("📱 You can now use the automated Airflow system")
    else:
        print("\n❌ Failed to post")
        print("🔧 Check the solutions above and try again")
    
    input("\nPress Enter to continue...")
