import argparse
import json
import csv
import os

def json_to_csv(input_file):
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

    # Get the output CSV file path
    output_file = os.path.splitext(input_file)[0]+'_output' + '.csv'

    # Write to the CSV file
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV file created successfully: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a JSON file to a CSV file.")
    parser.add_argument("input_file", help="Path to the input JSON file")
    args = parser.parse_args()

    json_to_csv(args.input_file)