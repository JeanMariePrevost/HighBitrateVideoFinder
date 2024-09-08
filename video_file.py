from functools import lru_cache
from pymediainfo import MediaInfo
import os
import zlib

class VideoFile:
    """
    A class to represent a video file.
    Handles various video file operations such as getting the duration, file size, and bitrate.
    
    Example usage:
    video_file = VideoFile("path_to_your_video.mp4")
    duration = video_file.get_duration()
    """
    
    def __init__(self, file_path):
        self.file_path = file_path

    @lru_cache(maxsize=None)
    def get_duration(self):
        """Returns the duration of the video in seconds."""
        media_info = MediaInfo.parse(self.file_path)
        for track in media_info.tracks:
            if track.track_type == 'Video':
                duration_in_ms = track.duration
                if duration_in_ms is not None:
                    return int(duration_in_ms) / 1000
        return None

    @lru_cache(maxsize=None)
    def get_filesize(self):
        """Returns the file size in bytes."""
        return os.path.getsize(self.file_path)

    @lru_cache(maxsize=None)
    def get_bitrate(self):
        """Calculates and returns the bitrate of the video in bits per second."""
        duration = self.get_duration()
        if duration is not None and duration > 0:
            filesize = self.get_filesize()  # in bytes
            return (filesize * 8) / duration
        return None

    @lru_cache(maxsize=None)
    def compute_partial_file_crc32(self, block_size=1048576 * 8):  # 8 MB by default
        """Computes the CRC32 hash of only the first block_size bytes of the video file."""
        file_hash = 0
        with open(self.file_path, 'rb') as f:
            fb = f.read(block_size)  # Read only the first block_size bytes
            file_hash = zlib.crc32(fb, file_hash)  # Compute CRC32 for the read portion
        
        return format(file_hash & 0xFFFFFFFF, '08x')