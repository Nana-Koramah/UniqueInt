
# Unique Integer Processor

## Overview

This Python script reads integers from an input file, identifies the unique integers, sorts them, and writes the sorted list to an output file. It handles non-integer lines gracefully by skipping them.

## How It Works

1. **Reading and Processing**:
   - Reads integers from the input file, skipping non-integer lines.
   - Uses a custom function to maintain a sorted list of unique integers.

2. **Writing Output**:
   - Writes the sorted unique integers to an output file, one integer per line.

## Usage

1. **Prerequisites**:
   - Python 3.x installed.

2. **Save the Script**:
   - Save the code in a file named `unique_integer_processor.py`.

3. **Prepare Input File**:
   - Create `input.txt` with integers, one per line.

4. **Run the Script**:
   ```bash
   python3 unique_integer_processor.py
   ```

## Example Input (`input.txt`)
```
5
14
5
-9
62
-1
-9
-9
```

## Example Output (`output.txt`)
```
-9
-1
5
14
62
```

## Code

```python
def read_and_process_file(input_file_path):
    """Read integers from file and return a sorted list of unique integers."""
    sorted_unique_integers = []
    with open(input_file_path, 'r') as file:
        for line in file:
            try:
                num = int(line.strip())
                sorted_unique_integers = custom_insert(sorted_unique_integers, num)
            except ValueError:
                continue  # Skip non-integer lines
    return sorted_unique_integers

def custom_insert(sorted_data, value):
    """Insert value into sorted_data maintaining sorted order."""
    if value in sorted_data:
        return sorted_data  # Skip insertion if value already exists.
    for i in range(len(sorted_data)):
        if value < sorted_data[i]:
            return sorted_data[:i] + [value] + sorted_data[i:]
    return sorted_data + [value]

def write_output_file(output_file_path, integers):
    """Write each integer from the list to the file, one per line."""
    with open(output_file_path, 'w') as file:
        for integer in integers:
            file.write(f"{integer}\n")

def process_file(input_file_path, output_file_path):
    """Process input file to generate an output file with sorted unique integers."""
    sorted_unique_integers = read_and_process_file(input_file_path)
    write_output_file(output_file_path, sorted_unique_integers)

# Example usage
input_file_path = 'input.txt'
output_file_path = 'output.txt'
process_file(input_file_path, output_file_path)
```

This concise README provides a clear overview, usage instructions, and the complete code for processing unique integers from an input file.
