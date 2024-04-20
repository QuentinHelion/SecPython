from network import *
from scan import *
import argparse

def main():
    print("Starting...")

    parser = argparse.ArgumentParser(description='Script with address and mask arguments')
    parser.add_argument('-a', '--address', required=True, help='This is address argument')
    parser.add_argument('-m', '--mask', default="24", help='This is mask argument')

    args = parser.parse_args()

    ip_range = calc(args.address, args.mask)

    for ip in ip_range:
        host(ip)


    print("Ending...")


if __name__ == "__main__":
    main()
