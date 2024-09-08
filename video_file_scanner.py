import os
import sys
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
    folder_count = 0
    file_count = 0
    
    # Recursively walk through the directory
    for root, _, files in os.walk(directory):
        folder_count += 1
        for file in files:
            if is_video_file(file):
                video_file = VideoFile(os.path.join(root, file))
                video_files.append(video_file)
                file_count += 1
                
                # Update the progress message
                sys.stdout.write(f"\r{file_count} video files found in {folder_count} folders (current folder: {root})")
                sys.stdout.flush()  # Ensure the output is written immediately

    # Print a final newline after completing the process
    sys.stdout.write("\n")
    
    return video_files