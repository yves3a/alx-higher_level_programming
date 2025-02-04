#!/usr/bin/env python3
import sys


def print_stats(total_size, status_codes):
    """Print the computed statistics"""
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    try:
        for line in sys.stdin:
            try:
                # Split the line and extract relevant parts
                parts = line.split()
                if len(parts) >= 9:
                    status_code = int(parts[-2])
                    file_size = int(parts[-1])

                    # Update metrics
                    if status_code in status_codes:
                        status_codes[status_code] += 1
                    total_size += file_size

                    line_count += 1
                    if line_count % 10 == 0:
                        print_stats(total_size, status_codes)

            except (ValueError, IndexError):
                continue

    except KeyboardInterrupt:

        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
