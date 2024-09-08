import os
from save_to_csv import save_to_csv
from video_file_scanner import scan_directory



if __name__ == "__main__":
    # Get directory input from the user
    directory = input("Enter the directory to scan for videos: ")

    # Scan the directory and list video files
    video_files = scan_directory(directory)
    
    #Print results overview
    print(f"\nFound {len(video_files)} video files in [{directory}]")
    
    # Print the detailled results
    input("Press Enter to display the details of the video files...")
    for video_file in video_files:
        filename = os.path.basename(video_file.file_path)
        bitrate_in_mbps = round(video_file.get_bitrate() / 1000000,1)
        size = video_file.get_filesize()
        length = video_file.get_duration()
        crc32 = video_file.compute_partial_file_crc32()
        print(f"File: {filename}\nBitrate: {bitrate_in_mbps} Mbps\nSize: {size} bytes\nLength: {length} seconds\nCRC32: {crc32}\n")
    
    
    
    # Save the results list to the CSV
    output_file = save_to_csv(video_files)

    print("Scan complete.")
    print(f"\n{len(video_files)} video files scanned and processed.")
    print(f"\nVideo files list saved to {output_file}.")
    input("Press Enter to exit...")
    exit(0)
    
    
    
