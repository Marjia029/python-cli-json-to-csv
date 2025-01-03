import argparse
import json
import csv
import os

def json_to_csv(input_file, output_file_path):
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    # Check if the input file is a JSON file
    if not input_file.endswith('.json'):
        print(f"Error: The file '{input_file}' is not a JSON file.")
        return

    # Read the JSON file
    with open(input_file, 'r') as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError:
            print(f"Error: The file '{input_file}' is not valid JSON.")
            return

    # Check if data is a list of dictionaries
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        print("Error: JSON data must be a list of dictionaries.")
        return
    
    if not os.path.exists(output_file_path):
        os.makedirs(output_file_path)

    # Get the output CSV file path
    input_file_name=os.path.basename(input_file).split('/')[-1]
    print(input_file_name)
    output_file_name = os.path.splitext(input_file_name)[0]+'_output' + '.csv'
    print(output_file_name)

    output_file_path=os.path.join(output_file_path, output_file_name)

    # Write to the CSV file
    with open(output_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV file created successfully: {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a JSON file to a CSV file.")
    parser.add_argument("input_file", help="Path to the input JSON file")
    parser.add_argument('output_file_path', help='Path to the output directory')
    args = parser.parse_args()

    json_to_csv(args.input_file, args.output_file_path)