#!/usr/bin/env python3

#!/usr/bin/env python3

def read_and_process_file(input_file_path):
    """Read integers from file and return a sorted list of unique integers."""
    unique_integers = set()
    with open(input_file_path, 'r') as file:
        for line in file:
            try:
                num = int(line.strip())
                unique_integers.add(num)
            except ValueError:
                continue  # Skip non-integer lines
    sorted_unique_integers = sorted(unique_integers)
    return sorted_unique_integers

def write_output_file(output_file_path, integers):
    """Write each integer from the list to the file, one per line."""
    with open(output_file_path, 'w') as file:
        for integer in integers:
            file.write(f"{integer}\n")

def process_file(input_file_path, output_file_path):
    """Process input file to generate an output file with sorted unique integers."""
    sorted_unique_integers = read_and_process_file(input_file_path)
    write_output_file(output_file_path, sorted_unique_integers)

if __name__ == "__main__":
    # Interactive input for file paths
    input_file_path = input("Enter the path to the input file: ")
    output_file_path = input("Enter the path to the output file: ")

    # Call the process_file function with user-provided paths
    process_file(input_file_path, output_file_path)
    print(f"Processed {input_file_path} and generated {output_file_path}")

