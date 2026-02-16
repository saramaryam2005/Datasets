"""
Performance benchmark comparing slow and optimized implementations
"""

import time
import sys
from data_processor_slow import (
    load_data_slow,
    count_spam_messages_slow,
    get_message_lengths_slow,
    find_long_messages_slow,
    calculate_statistics_slow,
    filter_spam_messages_slow
)
from data_processor_optimized import (
    load_data_fast,
    count_spam_messages_fast,
    get_message_lengths_fast,
    find_long_messages_fast,
    calculate_statistics_fast,
    filter_spam_messages_fast,
    analyze_with_counter,
    get_word_count_distribution
)


def benchmark_function(func, *args, iterations=3):
    """Run a function multiple times and return average execution time"""
    times = []
    result = None
    for _ in range(iterations):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        times.append(end - start)
    avg_time = sum(times) / len(times)
    return avg_time, result


def format_time(seconds):
    """Format time in appropriate units"""
    if seconds < 0.001:
        return f"{seconds * 1000000:.2f} μs"
    elif seconds < 1:
        return f"{seconds * 1000:.2f} ms"
    else:
        return f"{seconds:.2f} s"


def calculate_speedup(slow_time, fast_time):
    """Calculate speedup factor"""
    if fast_time > 0:
        return slow_time / fast_time
    return float('inf')


def main():
    print("=" * 70)
    print("PERFORMANCE BENCHMARK: Slow vs Optimized Data Processing")
    print("=" * 70)
    print()
    
    filename = 'spam.csv'
    
    # Benchmark 1: Load data
    print("1. Loading data...")
    slow_time, data_slow = benchmark_function(load_data_slow, filename)
    fast_time, data_fast = benchmark_function(load_data_fast, filename)
    speedup = calculate_speedup(slow_time, fast_time)
    
    print(f"   Slow method:      {format_time(slow_time)}")
    print(f"   Optimized method: {format_time(fast_time)}")
    print(f"   Speedup:          {speedup:.2f}x faster")
    print()
    
    # Benchmark 2: Count spam messages
    print("2. Counting spam messages...")
    slow_time, _ = benchmark_function(count_spam_messages_slow, data_slow)
    fast_time, _ = benchmark_function(count_spam_messages_fast, data_fast)
    speedup = calculate_speedup(slow_time, fast_time)
    
    print(f"   Slow method:      {format_time(slow_time)}")
    print(f"   Optimized method: {format_time(fast_time)}")
    print(f"   Speedup:          {speedup:.2f}x faster")
    print()
    
    # Benchmark 3: Get message lengths
    print("3. Calculating message lengths...")
    slow_time, _ = benchmark_function(get_message_lengths_slow, data_slow)
    fast_time, _ = benchmark_function(get_message_lengths_fast, data_fast)
    speedup = calculate_speedup(slow_time, fast_time)
    
    print(f"   Slow method:      {format_time(slow_time)}")
    print(f"   Optimized method: {format_time(fast_time)}")
    print(f"   Speedup:          {speedup:.2f}x faster")
    print()
    
    # Benchmark 4: Find long messages
    print("4. Finding long messages...")
    slow_time, _ = benchmark_function(find_long_messages_slow, data_slow, 100)
    fast_time, _ = benchmark_function(find_long_messages_fast, data_fast, 100)
    speedup = calculate_speedup(slow_time, fast_time)
    
    print(f"   Slow method:      {format_time(slow_time)}")
    print(f"   Optimized method: {format_time(fast_time)}")
    print(f"   Speedup:          {speedup:.2f}x faster")
    print()
    
    # Benchmark 5: Calculate statistics
    print("5. Calculating statistics...")
    slow_time, _ = benchmark_function(calculate_statistics_slow, data_slow)
    fast_time, _ = benchmark_function(calculate_statistics_fast, data_fast)
    speedup = calculate_speedup(slow_time, fast_time)
    
    print(f"   Slow method:      {format_time(slow_time)}")
    print(f"   Optimized method: {format_time(fast_time)}")
    print(f"   Speedup:          {speedup:.2f}x faster")
    print()
    
    # Benchmark 6: Filter spam messages
    print("6. Filtering spam messages...")
    slow_time, _ = benchmark_function(filter_spam_messages_slow, data_slow)
    fast_time, _ = benchmark_function(filter_spam_messages_fast, data_fast)
    speedup = calculate_speedup(slow_time, fast_time)
    
    print(f"   Slow method:      {format_time(slow_time)}")
    print(f"   Optimized method: {format_time(fast_time)}")
    print(f"   Speedup:          {speedup:.2f}x faster")
    print()
    
    # Additional optimized-only benchmarks
    print("7. Label analysis with Counter (optimized only)...")
    fast_time, result = benchmark_function(analyze_with_counter, data_fast)
    print(f"   Optimized method: {format_time(fast_time)}")
    print(f"   Result: {dict(result)}")
    print()
    
    print("8. Word count distribution (optimized only)...")
    fast_time, result = benchmark_function(get_word_count_distribution, data_fast)
    print(f"   Optimized method: {format_time(fast_time)}")
    print(f"   Top 5 word counts: {result.most_common(5)}")
    print()
    
    print("=" * 70)
    print("SUMMARY OF IMPROVEMENTS")
    print("=" * 70)
    print()
    print("Key optimizations applied:")
    print("  • List comprehensions instead of repeated list concatenation")
    print("  • Generator expressions for memory efficiency")
    print("  • Single-pass algorithms instead of multiple iterations")
    print("  • String join() instead of repeated concatenation")
    print("  • Direct iteration instead of range(len())")
    print("  • Built-in collections.Counter for frequency analysis")
    print()


if __name__ == "__main__":
    main()
