import datetime
import os
import csv
import sys
from video_file import VideoFile
from video_file_scanner import scan_directory



if __name__ == "__main__":
    # Get directory input from the user
    directory = input("Enter the directory to scan for videos: ")

    # Scan the directory and list video files
    video_files = scan_directory(directory)
    
    #Print results overview
    print(f"\nFound {len(video_files)} video files in [{directory}]")
    
    # DEBUG: calcualte time needed to get the size of all video files
    print("#" * 20)
    print("Calculating the size of all video files...")
    start_time = datetime.datetime.now()
    for video_file in video_files:
        print(video_file.get_filesize())
    end_time = datetime.datetime.now()
    print(f"Time needed to get the size of all video files: {end_time - start_time}")
    print("#" * 20)

    #DEBUG: calculate time needed to get the duration of all video files
    print("#" * 20)
    print("Calculating the duration of all video files...")
    start_time = datetime.datetime.now()
    for video_file in video_files:
        print(video_file.get_duration())
    end_time = datetime.datetime.now()
    print(f"Time needed to get the duration of all video files: {end_time - start_time}")
    print("#" * 20)
    
    #DEBUG: calculate time needed to get the bitrate of all video files
    print("#" * 20)
    print("Calculating the bitrate of all video files...")
    start_time = datetime.datetime.now()
    for video_file in video_files:
        print(video_file.get_bitrate())
    end_time = datetime.datetime.now()
    print(f"Time needed to get the bitrate of all video files: {end_time - start_time}")
    print("#" * 20)
    
    #DEBUG: calculate time needed to get the partial crc32 of all video files
    print("#" * 20)
    print("Calculating the partial crc32 of all video files...")
    start_time = datetime.datetime.now()
    for video_file in video_files:
        print(video_file.compute_partial_file_crc32())
    end_time = datetime.datetime.now()
    print(f"Time needed to get the partial crc32 of all video files: {end_time - start_time}")
    print("#" * 20)
    
    
    # Define a name and path for the CSV file, using a timestamp
    # output_file = os.path.join(os.path.dirname(__file__), f"video_files_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.csv")

    # Save the results list to the CSV
    # save_to_csv(video_files, output_file)

    # print(f"\nVideo files list saved to {output_file}.")
    
    
    
