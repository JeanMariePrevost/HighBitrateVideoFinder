class VideoFileFromCSV:
    """
    A static version of the VideoFile class that uses provided information instead of reading it from a file.
    
    Example usage:
    static_video_file = VideoFileFromCSV(file_path="path_to_your_video.mp4", duration=300, filesize=50000000, crc32="d87f7e0c")
    bitrate = static_video_file.get_bitrate()
    """
    
    def __init__(self, file_path, bitrate, duration, filesize, crc32):
        self.file_path = file_path
        self._bitrate = bitrate # In Mbits per second
        self._duration = duration  # In seconds
        self._filesize = filesize  # In MB
        self._crc32 = crc32  # Precomputed CRC32 hash
    
    def get_duration(self):
        """Returns the duration of the video in seconds (already provided)."""
        return self._duration

    def get_filesize(self):
        """Returns the file size in bytes (already provided)."""
        return self._filesize

    def get_bitrate(self):
        """Returns the bitrate of the video in bits per second (already provided)."""
        return self._bitrate

    def compute_partial_file_crc32(self):
        """Returns the precomputed CRC32 hash."""
        return self._crc32
