print("io")


# Define input and output file paths
input_file = './src/data/data.txt'

# Open the input text file for reading
with open(input_file, 'r') as txt_file:
    # Read the lines from the text file
    lines = txt_file.readlines()
    print(lines)