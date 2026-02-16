# Performance Optimization Guide

This repository demonstrates common performance issues in Python data processing and their optimized solutions.

## Overview

The code examples work with the spam.csv dataset and demonstrate:
- **Inefficient patterns** that lead to slow execution
- **Optimized alternatives** using Python best practices
- **Measurable performance improvements**

## Files

- `data_processor_slow.py` - Examples of inefficient code patterns
- `data_processor_optimized.py` - Optimized versions of the same operations
- `benchmark.py` - Performance comparison tool

## Common Performance Issues & Solutions

### 1. List Concatenation in Loops ❌

**Inefficient:**
```python
data = []
for row in reader:
    data = data + [row]  # Creates new list each time - O(n²)
```

**Optimized:**
```python
data = [row for row in reader]  # List comprehension - O(n)
```

**Why:** List concatenation (`list1 + list2`) creates a new list and copies all elements, resulting in O(n²) complexity. List comprehensions build the list in a single pass.

### 2. Multiple Iterations Over Data ❌

**Inefficient:**
```python
# First pass
spam_count = sum(1 for row in data if row[0] == 'spam')
# Second pass
ham_count = sum(1 for row in data if row[0] == 'ham')
# Third pass
total_length = sum(len(row[1]) for row in data)
```

**Optimized:**
```python
# Single pass
spam_count = ham_count = total_length = 0
for row in data:
    if row[0] == 'spam':
        spam_count += 1
    elif row[0] == 'ham':
        ham_count += 1
    total_length += len(row[1])
```

**Why:** Each iteration over data has overhead. Combining operations reduces this overhead significantly.

### 3. String Concatenation in Loops ❌

**Inefficient:**
```python
result = ""
for row in data:
    result = result + row[0] + "\n"  # Creates new string each time
```

**Optimized:**
```python
result = "\n".join(row[0] for row in data)  # Join once at the end
```

**Why:** Strings are immutable in Python. Concatenation creates new string objects, while `join()` allocates memory once.

### 4. Using range(len()) Instead of Direct Iteration ❌

**Inefficient:**
```python
for i in range(len(data)):
    process(data[i])
```

**Optimized:**
```python
for row in data:
    process(row)
```

**Why:** Direct iteration is more Pythonic, readable, and slightly faster as it avoids index lookups.

### 5. Not Using Built-in Tools ❌

**Inefficient:**
```python
label_counts = {}
for row in data:
    label = row[0]
    if label not in label_counts:
        label_counts[label] = 0
    label_counts[label] += 1
```

**Optimized:**
```python
from collections import Counter
label_counts = Counter(row[0] for row in data)
```

**Why:** Python's built-in collections are implemented in C and highly optimized.

## Running the Examples

### Run the slow version:
```bash
python data_processor_slow.py
```

### Run the optimized version:
```bash
python data_processor_optimized.py
```

### Run the benchmark:
```bash
python benchmark.py
```

## Expected Performance Improvements

Based on the dataset (5,572 messages), you should see:

- **List operations:** 10-50x faster
- **String operations:** 20-100x faster  
- **Statistics calculation:** 3-5x faster
- **Overall processing:** 5-20x faster

Actual speedup depends on dataset size and system performance.

## Best Practices Summary

1. ✅ Use list comprehensions instead of repeated append/concatenation
2. ✅ Use generator expressions for memory efficiency
3. ✅ Minimize iterations over large datasets
4. ✅ Use `str.join()` instead of string concatenation in loops
5. ✅ Leverage built-in functions and collections (Counter, defaultdict, etc.)
6. ✅ Profile your code to identify actual bottlenecks
7. ✅ Consider using pandas for large-scale data processing

## Additional Resources

- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
- [collections module documentation](https://docs.python.org/3/library/collections.html)
- [Time Complexity of Python Operations](https://wiki.python.org/moin/TimeComplexity)

## License

Apache License 2.0 - See LICENSE file for details
