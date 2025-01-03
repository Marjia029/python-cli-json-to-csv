import argparse
import json
import csv

def load_json(filename):
    json_file = open(filename, 'r')
    json_data = json.load(json_file)
    print(json_data)

    with open("Output.csv", 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=json_data[0].keys())
        writer.writeheader()
        writer.writerows(json_data)


   

def main():
    parser = argparse.ArgumentParser(description='Load a JSON file.')
    parser.add_argument('filename', help='Path to the JSON file')
    args = parser.parse_args()

    load_json(args.filename)

if __name__ == '__main__':
    main()