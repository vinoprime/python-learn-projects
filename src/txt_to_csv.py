import csv

# Define input and output file paths
input_file = 'data_0.txt'
output_file = 'output.csv'

# Open the input text file for reading
with open(input_file, 'r') as txt_file:
    # Read the lines from the text file
    lines = txt_file.readlines()

# Open the output CSV file for writing
with open(output_file, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the header (assuming the header is the first line in the text file)
    header = lines[0].strip().split(',')
    csv_writer.writerow(header)

    # Write the data (skipping the first line, which is the header)
    for line in lines[1:]:
        data = line.strip().split(',')
        csv_writer.writerow(data)

print(f'Conversion complete. CSV file saved as {output_file}')
