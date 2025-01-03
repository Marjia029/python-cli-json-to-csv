import argparse

parser = argparse.ArgumentParser(description='This is a new command-line tool')

parser.add_argument('input_file', help='Path to the input file')

args = parser.parse_args()

print(f'Input file: {args.input_file}')

parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose mode')

