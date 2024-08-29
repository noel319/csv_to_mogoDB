import csv
import pandas as pd

# Function to detect the delimiter
def detect_delimiter(file_path):
    with open(file_path, 'r') as file:
        sample = file.read(1024)  # Read a sample of the file
        sniffer = csv.Sniffer()
        delimiter = sniffer.sniff(sample).delimiter
    return delimiter

# Function to read the file with the detected delimiter
def read_file_with_detected_delimiter(file_path):
    delimiter = detect_delimiter(file_path)
    print(f"Detected delimiter: '{delimiter}'")
    data = pd.read_csv(file_path, delimiter=delimiter)
    return data

# Example usage
file_path = 'data/test_file_1.csv'  # or 'path_to_your_file.txt'
data = read_file_with_detected_delimiter(file_path)
print(data)
