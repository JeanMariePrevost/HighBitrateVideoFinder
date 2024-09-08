import csv
import datetime
import os
from video_file import VideoFile


def save_to_csv(video_files):
    """Saves the list of video files to a CSV file."""
    
    # Output file at script location in "results" directory, timestamped
    # Ensure the "results" directory exists
    results_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(results_dir, exist_ok=True)
    
    # Create the output file path within the "results" directory
    output_file = os.path.join(results_dir, f"video_files_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.csv")
    
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(
            [
                "File",
                "Bitrate (Mbps)",
                "Size (MB)",
                "Length (seconds)",
                "CRC32 (Partial)",
            ]
        )

        # Write the data rows, with formatting and rounding
        for video_file in video_files:
            file = video_file.file_path
            bitrate_in_mbps = f"{video_file.get_bitrate() / 1_000_000:.1f}"  # Format to 1 decimal place
            size_in_mb = f"{video_file.get_filesize() / (1024 * 1024):.1f}"  # Format to 1 decimal place
            length = f"{video_file.get_duration():.1f}"  # Format to 1 decimal place
            crc32 = video_file.compute_partial_file_crc32()
            writer.writerow([file, bitrate_in_mbps, size_in_mb, length, crc32])
    return output_file


