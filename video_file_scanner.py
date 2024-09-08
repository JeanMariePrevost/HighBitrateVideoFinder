import os
from video_file import VideoFile

"""
This module contains the logic for scanning a directory for video files and returning a list of VideoFile objects.
"""

# List of common video file extensions
VIDEO_EXTENSIONS = ['.mp4', '.mkv', '.avi', '.ts', '.mov', '.wmv', '.flv', '.mpeg', '.webm']

# Function to check if a file is a video file
def is_video_file(filename):
    return any(filename.lower().endswith(ext) for ext in VIDEO_EXTENSIONS)

# Function to scan a directory for video files, returns a list of VideoFile objects
def scan_directory(directory):
    """Recursively scan a directory for video files and return a list of VideoFile objects."""
    video_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if is_video_file(file):
                video_file = VideoFile(os.path.join(root, file))
                video_files.append(video_file)
    
    return video_files
