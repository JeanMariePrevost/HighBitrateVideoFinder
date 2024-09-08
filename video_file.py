from functools import lru_cache
import os
import hashlib
import ffmpeg
from moviepy.editor import VideoFileClip
from pymediainfo import MediaInfo

class VideoFile:
    """
    Class representing a video file with its attributes.
    Also handles everything related to the video file, like figuring out its bitrate, length, hash...
    
    Example usage:
    video_file = VideoFile('path/to/video.mp4')
    print(video_file.size)  # File size in bytes
    print(video_file.compute_file_hash())  # Get the file hash
    """
    
    def __init__(self, file_path):
        self.file_path = file_path


    @lru_cache(maxsize=None)
    def get_clip(self):
        return VideoFileClip(self.file_path)
    
    @lru_cache(maxsize=None)
    def get_duration(self):
        return self.get_clip().duration  # Duration in seconds
    
    @lru_cache(maxsize=None)
    def get_filesize(self):
        return os.path.getsize(self.file_path)  # File size in bytes
    
    @lru_cache(maxsize=None)
    def get_bitrate(self):
        return (self.get_filesize() * 8) / self.get_duration()  # Bitrate in bits per second
    
    
    

    @lru_cache(maxsize=None)
    def get_duration_ffmpeg(self):
        try:
            probe = ffmpeg.probe(self.file_path)
            video_streams = [stream for stream in probe['streams'] if stream['codec_type'] == 'video']
            if video_streams:
                video_stream = video_streams[0]
                # Check if 'duration' key exists in the video stream dictionary
                if 'duration' in video_stream:
                    duration = float(video_stream['duration'])
                    return duration
                else:
                    print("Duration key not found in video stream metadata.")
            else:
                print("No video streams found in the file.")
        except ffmpeg.Error as e:
            print("An error occurred while probing the file:", e)
        return None

    @lru_cache(maxsize=None)
    def get_duration_mediainfo(self):
        try:
            media_info = MediaInfo.parse(self.file_path)
            for track in media_info.tracks:
                if track.track_type == 'Video':
                    duration_in_ms = track.duration
                    if duration_in_ms is not None:
                        duration_in_seconds = int(duration_in_ms) / 1000
                        return duration_in_seconds
            print("No Video track found in file.")
        except Exception as e:
            print("An error occurred while reading the file:", e)
        return None

    @lru_cache(maxsize=None)
    def compute_file_hash(self, hash_algorithm='sha256'):
        """Compute a hash for the video file using its content."""
        hash_func = hashlib.new(hash_algorithm)
        with open(self.file_path, 'rb') as f:
            while chunk := f.read(8192):  # Read file in chunks
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def to_dict(self):
        """Convert the object to a dictionary for easy CSV export."""
        return {
            'Video File Path': self.file_path,
            'File Size (Bytes)': self.size,
            'File Hash': self.hash,
        }


