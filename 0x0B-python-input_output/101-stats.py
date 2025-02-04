#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import sys


def print_stats(total_size, status_codes):
    """Print accumulated statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    """Main function to process input and compute metrics"""
    total_size = 0
    line_count = 0
    status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                # Split the line and extract relevant parts
                parts = line.split()
                if len(parts) > 2:  # Ensure we have at least some parts
                    # File size will be the last element
                    size = parts[-1]
                    # Status code will be second to last element
                    code = parts[-2]

                    if code in status_codes:
                        status_codes[code] += 1
                    try:
                        total_size += int(size)
                    except ValueError:
                        line_count -= 1
                        continue

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

            except (IndexError, ValueError):
                line_count -= 1
                continue

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
