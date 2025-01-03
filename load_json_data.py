import argparse
import json
import csv
import os

def load_json(filename, output_file_path):
    json_file = open(filename, 'r')
    json_data = json.load(json_file)
    print(json_data)

    # with open("Output.csv", 'w', newline='') as csv_file:
    #     writer = csv.DictWriter(csv_file, fieldnames=json_data[0].keys())
    #     writer.writeheader()
    #     writer.writerows(json_data)

    if not os.path.exists(output_file_path):
        os.makedirs(output_file_path)
    
    output_file_path=os.path.join(output_file_path, 'output.csv')

    with open(output_file_path, 'w', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=json_data[0].keys())
        writer.writeheader()
        writer.writerows(json_data)

def main():
    parser = argparse.ArgumentParser(description='Load a JSON file.')
    parser.add_argument('filename', help='Path to the JSON file')
    parser.add_argument('output_file_path', help='Path to the output directory')
    args = parser.parse_args()

    load_json(args.filename, args.output_file_path)

if __name__ == '__main__':
    main()