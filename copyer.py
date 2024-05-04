import os
import shutil

def copy_videos():
    source_dir = r'where to store vids'
    
    destination_dir = r'path to phone'
    
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    for file in os.listdir(source_dir):
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(destination_dir, file)
        
        if is_video(file):
            
            shutil.copy2(source_path, destination_path)
            print(f"Copied {file} to {destination_dir}")

def is_video(filename):
    
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm']
   
    return any(filename.lower().endswith(ext) for ext in video_extensions)


copy_videos()
