"""
Optimized data processing example - demonstrating performance best practices
This script loads and processes spam.csv in an efficient way
"""

import csv
from collections import Counter


def load_data_fast(filename):
    """Optimized: Using list comprehension and efficient file reading"""
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        # Efficient: List comprehension builds list in one pass
        return [row for row in reader]


def count_spam_messages_fast(data):
    """Optimized: Direct iteration with generator expression"""
    # Efficient: Single pass with generator expression
    return sum(1 for row in data if row[0] == 'spam')


def get_message_lengths_fast(data):
    """Optimized: List comprehension"""
    # Efficient: List comprehension is faster than repeated append
    return [len(row[1]) if len(row) > 1 else 0 for row in data]


def find_long_messages_fast(data, threshold=100):
    """Optimized: Using list and join instead of string concatenation"""
    # Efficient: Building list then joining once
    messages = [
        f"{row[0]}: {row[1][:50]}..."
        for row in data
        if len(row) > 1 and len(row[1]) > threshold
    ]
    return "\n".join(messages)


def calculate_statistics_fast(data):
    """Optimized: Single pass over data"""
    # Efficient: Calculate all statistics in a single iteration
    spam_count = 0
    ham_count = 0
    total_length = 0
    max_length = 0
    
    for row in data:
        label = row[0]
        if label == 'spam':
            spam_count += 1
        elif label == 'ham':
            ham_count += 1
        
        if len(row) > 1:
            msg_len = len(row[1])
            total_length += msg_len
            max_length = max(max_length, msg_len)
    
    return {
        'spam_count': spam_count,
        'ham_count': ham_count,
        'avg_length': total_length / len(data) if data else 0,
        'max_length': max_length
    }


def filter_spam_messages_fast(data):
    """Optimized: List comprehension for filtering"""
    # Efficient: List comprehension is faster than repeated append
    return [row for row in data if row[0] == 'spam']


def analyze_with_counter(data):
    """Optimized: Using Counter for frequency analysis"""
    # Efficient: Counter optimized for counting operations
    labels = Counter(row[0] for row in data)
    return labels


def get_word_count_distribution(data):
    """Optimized: Efficient word counting with generator"""
    # Efficient: Generator expression with map
    word_counts = [
        len(row[1].split()) if len(row) > 1 else 0 
        for row in data
    ]
    return Counter(word_counts)


def main():
    print("Loading data (fast method)...")
    data = load_data_fast('spam.csv')
    print(f"Loaded {len(data)} messages")
    
    print("\nCounting spam messages (fast method)...")
    spam_count = count_spam_messages_fast(data)
    print(f"Found {spam_count} spam messages")
    
    print("\nCalculating message lengths (fast method)...")
    lengths = get_message_lengths_fast(data)
    print(f"Processed {len(lengths)} message lengths")
    
    print("\nFinding long messages (fast method)...")
    long_msgs = find_long_messages_fast(data, 100)
    print(f"Found {len([m for m in long_msgs.split('\n') if m])} long messages")
    
    print("\nCalculating statistics (fast method)...")
    stats = calculate_statistics_fast(data)
    print(f"Statistics: {stats}")
    
    print("\nFiltering spam messages (fast method)...")
    spam_only = filter_spam_messages_fast(data)
    print(f"Filtered to {len(spam_only)} spam messages")
    
    print("\nAnalyzing with Counter (fast method)...")
    label_counts = analyze_with_counter(data)
    print(f"Label distribution: {dict(label_counts)}")
    
    print("\nWord count distribution (fast method)...")
    word_dist = get_word_count_distribution(data)
    print(f"Top 5 word counts: {word_dist.most_common(5)}")


if __name__ == "__main__":
    main()
