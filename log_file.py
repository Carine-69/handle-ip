import heapq
from collections import defaultdict

# Function to read the file and aggregate request counts by IP address
def addresses(file_path):
    ip_counts = defaultdict(int)
    try:
        with open(file_path, 'r') as f:  # Open file at file_path
            for line in f:  # Iterate through each line in the file
                identifiers = line.strip().split(',')  # Split each line by commas and remove whitespaces
                if len(identifiers) == 3:  # Check if a line has exactly three parts
                    _, ip_address, requests = identifiers  # Extract IP address and requests count
                    try:
                        ip_counts[ip_address.strip()] += int(requests.strip())  # Add requests to the IP's total
                    except ValueError:
                        print(f"Skipping line with invalid request count: {line.strip()}")
                else:
                    print(f"Skipping malformed line: {line.strip()}")  # Handle lines with unexpected formats
    except FileNotFoundError:
        print(f"File '{file_path}' not found")  # Handle if file does not exist
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")  # Handle any other errors
    return ip_counts  # Return total counts for each IP

# Function to retrieve the top N IP addresses
def get_top_N(ip_counts, n):
    min_heap = []  # Initialize a min heap to keep the top N IPs by requests
    for ip, count in ip_counts.items():  # Iterate over each IP and its total request count
        heapq.heappush(min_heap, (count, ip))  # Push IPs and request counts into the min heap
        if len(min_heap) > n:
            heapq.heappop(min_heap)  # Ensure min heap only contains the top N items
    return sorted(min_heap, key=lambda x: (-x[0], x[1]))  # Sort by requests descending and IP lexicographically

# Function to write output to a file
def keep_results(output_file_path, top_n):
    try:
        with open(output_file_path, 'w') as f:  # Open output file for writing
            for rank, (count, ip) in enumerate(top_n, start=1):
                f.write(f"{rank},{ip},{count}\n")  # Format: rank, IP, request count
    except Exception as e:
        print(f"An error occurred while writing results: {e}")  # Handle any error in writing results

# Main function for execution
def main(log_file_path, output_file_path, n):
    ip_counts = addresses(log_file_path)  # Get IPs and requests from the file
    if not ip_counts:
        print("No IP counts were found")  # If no counts were found
        return
    top_n = get_top_N(ip_counts, n)  # Find the top N IPs by request count
    keep_results(output_file_path, top_n)
    print(f"Top {n} IPs have been written to '{output_file_path}'")

# Example usage
main('sample_input.txt', 'output.txt', 1)
