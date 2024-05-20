#!/usr/bin/env python3

def read_and_sort_file(input_file_path):
    """ Read integers from file and return a list of unique integers in ascending order. """
    sorted_unique_integers = []
    with open(input_file_path, 'r') as file:
        for line in file:
            try:
                num = int(line.strip())
                sorted_unique_integers = value_insert(sorted_unique_integers, num)
            except ValueError:
                continue  # Skip non-integer lines
    return sorted_unique_integers

def value_insert(sorted_data, value):
    """ Insert value into the list while maintaining the sorted order. """
    if value in sorted_data:
        return sorted_data  # Skip insertion if value already exists.
    for i in range(len(sorted_data)):
        if value < sorted_data[i]:
            sorted_data = sorted_data[:i] + [value] + sorted_data[i:]
            return sorted_data
    sorted_data.append(value)
    return sorted_data

def write_output_file(output_file_path, integers):
    """ Write each integer from the list to the output file, one per line. """
    with open(output_file_path, 'w') as file:
        for integer in integers:
            file.write(f"{integer}\n")

def process_file(input_file_path, output_file_path):
    """ Process input file to generate an output file with sorted unique integers. """
    sorted_unique_integers = read_and_sort_file(input_file_path)
    write_output_file(output_file_path, sorted_unique_integers)

# Example usage
input_file_path = 'small_sample_input_01.txt'
output_file_path = 'output.txt'
process_file(input_file_path, output_file_path)
