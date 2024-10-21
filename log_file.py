import os

# Open the file for reading
with open('sample_input.txt', 'r') as f:
    # Read the file line by line
    for line in f:
        # Split the line by commas
        contents = line.strip().split(',')

        # Extract the IP address (second element)
        ip_address = contents[1].strip()

        # Ping the IP address
        response = os.popen(f'ping  {ip_address}').read()  # Ping once (-c 1)

        # Print the ping response
        print(response)

