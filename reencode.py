import os
import glob
from video_file_from_csv import VideoFileFromCSV

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get a list of all CSV files in the current directory and /results/ folder
csv_files = glob.glob(os.path.join(current_dir, '*.csv'))
csv_files += glob.glob(os.path.join(current_dir, 'results', '*.csv'))

# Sort the CSV files by modification time in descending order
csv_files.sort(key=os.path.getmtime, reverse=True)

# Get the 5 most recent CSV files
recent_csv_files = csv_files[:5]

# Print the list of recent CSV files, showing a number followed by the filename only
print("Recent CSV files:")
for i, csv_file in enumerate(recent_csv_files):
    print(f"{i + 1}. {os.path.basename(csv_file)}")

# Ask the user to select a CSV file
selected_csv_file = None
while selected_csv_file is None:
    try:
        selection = int(input("Select a CSV file to re-encode: "))
        selected_csv_file = recent_csv_files[selection - 1]
    except (ValueError, IndexError):
        print("Invalid selection. Please enter a number from the list.")


# Buld a list of VideoFileFromCSV objects from the selected CSV file
video_files = []
with open(selected_csv_file, 'r', encoding="utf-8-sig") as file:
    next(file)  # Skip the header row
    for line in file:
        parts = line.strip().split(',')
        if len(parts) == 5:
            new_video_file = VideoFileFromCSV(file_path=parts[0], bitrate=float(parts[1]), duration=float(parts[3]), filesize=float(parts[2]), crc32=parts[4])
            video_files.append(new_video_file)
        

# Print the number of video files loaded from the CSV
print(f"\nLoaded {len(video_files)} video files from [{selected_csv_file}].")

# Print a peek of the selected CSV file in the following format:
# [Bitrate (Mbps)] [Size (MB)] [CRC32 (Partial)] [File]
def print_row(bitrate, size, crc32, filename):
    print(f"{bitrate:>15} {size:>11} {crc32:>18}   {filename[:60]}")

# Number of rows to print
peek_first_n = 3  # Number of first rows to print
peek_last_n = 3  # Number of last rows to print

print("\nPreview of the selected CSV file:")
print_row("Bitrate (Mbps)", "Size (MB)", "CRC32 (Partial)", "File")
print_row("--------------", "---------", "----------------", "----")
for video_file in video_files[:peek_first_n]:
    print_row(video_file.get_bitrate(), video_file.get_filesize(), video_file.compute_partial_file_crc32(), video_file.file_path)
print("    ...")
for video_file in video_files[-peek_last_n:]:
    print_row(video_file.get_bitrate(), video_file.get_filesize(), video_file.compute_partial_file_crc32(), video_file.file_path)



# Ask the user for a threshold bitrate, display the number of matches, ask for confirmation, loop if the user refuses
threshold_bitrate = None
while threshold_bitrate is None:
    try:
        threshold_bitrate = float(input("\nEnter the threshold bitrate (Mbps) to filter by: "))
    except ValueError:
        print("Invalid input. Please enter a number.")

# Filter the video files by the threshold bitrate
filtered_video_files = [video_file for video_file in video_files if video_file.get_bitrate() >= threshold_bitrate]
print(f"\nFound {len(filtered_video_files)} video files with a bitrate greater than or equal to {threshold_bitrate} Mbps.")
input("Re-encode these files? Press Enter to continue or Ctrl+C to cancel...")

print("Not implemented yet.")
print("Exiting...")
