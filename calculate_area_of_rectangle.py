import argparse

def calculate_area(length, width):
    area = length * width
    return area

def main():
    print("Hii") 
    parser = argparse.ArgumentParser(description='Calculate the area of a rectangle.')

    parser.add_argument('length', type=float, help='Length of the rectangle')
    parser.add_argument('width', type=float, help='Width of the rectangle')

    args = parser.parse_args()

    area = calculate_area(args.length, args.width)
    print(f"The area of the rectangle is: {area}")


if __name__ == '__main__':
        main()