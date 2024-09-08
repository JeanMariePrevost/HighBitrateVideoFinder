from save_to_csv import save_to_csv
from video_file_scanner import scan_directory
from tqdm import tqdm



if __name__ == "__main__":
    # Get directory input from the user
    directory = input("Enter the directory to scan for videos: ")

    # Scan the directory and list video files
    video_files = scan_directory(directory)
    
    #Print results overview
    print(f"\nFound {len(video_files)} video files in [{directory}]")
    
    
    # Extract/compute (and cache) the metadata
    print("\nProcessing video files...")
    for video_file in tqdm(video_files, unit="file"):
        video_file.get_filesize()
    
    print("\nComputing partial CRC32...")
    for video_file in tqdm(video_files, unit="file"):
        video_file.compute_partial_file_crc32()
    
    print("\nClaculating bitrates... (This is the slowest step)")
    for video_file in tqdm(video_files, unit="file"):
        video_file.get_bitrate()
    
    
    #sort the video files by bitrate
    print("\nSorting video files by bitrate...")
    video_files.sort(key=lambda x: x.get_bitrate(), reverse=True)
        
    # Save the results list to the CSV
    print("\nSaving results to CSV...")
    output_file = save_to_csv(video_files)

    print("\n\nScan complete.")
    print(f"{len(video_files)} video files scanned and processed.")
    print(f"Video files list saved to {output_file}.")
    input("Press Enter to exit...")
    exit(0)
    
    
    
