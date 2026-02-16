"""
Inefficient data processing example - demonstrating common performance issues
This script loads and processes spam.csv in an inefficient way
"""

import csv


def load_data_slow(filename):
    """Inefficient: Reading file line by line with multiple list operations"""
    data = []
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            # Inefficient: Creating new list on each append
            data = data + [row]
    return data


def count_spam_messages_slow(data):
    """Inefficient: Multiple iterations over the data"""
    spam_count = 0
    for i in range(len(data)):
        # Inefficient: Using range(len()) instead of direct iteration
        if data[i][0] == 'spam':
            spam_count = spam_count + 1
    return spam_count


def get_message_lengths_slow(data):
    """Inefficient: Building list with repeated concatenation"""
    lengths = []
    for i in range(len(data)):
        message = data[i][1] if len(data[i]) > 1 else ""
        # Inefficient: List concatenation in loop
        lengths = lengths + [len(message)]
    return lengths


def find_long_messages_slow(data, threshold=100):
    """Inefficient: String concatenation in loop"""
    result = ""
    for row in data:
        if len(row) > 1:
            message = row[1]
            if len(message) > threshold:
                # Inefficient: String concatenation in loop
                result = result + row[0] + ": " + message[:50] + "...\n"
    return result


def calculate_statistics_slow(data):
    """Inefficient: Multiple passes over data"""
    # First pass: count spam
    spam_count = 0
    for row in data:
        if row[0] == 'spam':
            spam_count += 1
    
    # Second pass: count ham
    ham_count = 0
    for row in data:
        if row[0] == 'ham':
            ham_count += 1
    
    # Third pass: get lengths
    total_length = 0
    for row in data:
        if len(row) > 1:
            total_length += len(row[1])
    
    # Fourth pass: find max length
    max_length = 0
    for row in data:
        if len(row) > 1:
            msg_len = len(row[1])
            if msg_len > max_length:
                max_length = msg_len
    
    return {
        'spam_count': spam_count,
        'ham_count': ham_count,
        'avg_length': total_length / len(data) if data else 0,
        'max_length': max_length
    }


def filter_spam_messages_slow(data):
    """Inefficient: Creating new list with repeated operations"""
    spam_messages = []
    for row in data:
        if row[0] == 'spam':
            # Inefficient: List concatenation
            spam_messages = spam_messages + [row]
    return spam_messages


def main():
    print("Loading data (slow method)...")
    data = load_data_slow('spam.csv')
    print(f"Loaded {len(data)} messages")
    
    print("\nCounting spam messages (slow method)...")
    spam_count = count_spam_messages_slow(data)
    print(f"Found {spam_count} spam messages")
    
    print("\nCalculating message lengths (slow method)...")
    lengths = get_message_lengths_slow(data)
    print(f"Processed {len(lengths)} message lengths")
    
    print("\nFinding long messages (slow method)...")
    long_msgs = find_long_messages_slow(data, 100)
    print(f"Found {len([m for m in long_msgs.split('\n') if m])} long messages")
    
    print("\nCalculating statistics (slow method)...")
    stats = calculate_statistics_slow(data)
    print(f"Statistics: {stats}")
    
    print("\nFiltering spam messages (slow method)...")
    spam_only = filter_spam_messages_slow(data)
    print(f"Filtered to {len(spam_only)} spam messages")


if __name__ == "__main__":
    main()
