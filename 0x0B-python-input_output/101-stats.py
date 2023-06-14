#!/usr/bin/python3

import sys

def print_stats(total_size, status_counts):
    """Print the computed statistics"""
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_counts.keys())
    for code in sorted_status_codes:
        count = status_counts[code]
        print("{}: {}".format(code, count))

def parse_line(line):
    """Parse a line of input and extract relevant information"""
    parts = line.split()
    if len(parts) < 7:
        return None, None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = int(parts[-1])
    return status_code, file_size

def compute_metrics():
    """Compute the metrics based on the input"""
    total_size = 0
    status_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line = line.strip()
            status_code, file_size = parse_line(line)
            if status_code is None or file_size is None:
                continue
            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

compute_metrics()
