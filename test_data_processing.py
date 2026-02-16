"""
Unit tests for data processing functions
"""

import unittest
from data_processor_slow import (
    load_data_slow,
    count_spam_messages_slow,
    get_message_lengths_slow,
    calculate_statistics_slow,
    filter_spam_messages_slow
)
from data_processor_optimized import (
    load_data_fast,
    count_spam_messages_fast,
    get_message_lengths_fast,
    calculate_statistics_fast,
    filter_spam_messages_fast,
    analyze_with_counter
)


class TestDataProcessing(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Load data once for all tests"""
        cls.data_slow = load_data_slow('spam.csv')
        cls.data_fast = load_data_fast('spam.csv')
    
    def test_load_data_consistency(self):
        """Test that both loading methods produce the same data"""
        self.assertEqual(len(self.data_slow), len(self.data_fast))
        self.assertEqual(len(self.data_slow), 5572)
        
        # Check first and last rows match
        self.assertEqual(self.data_slow[0], self.data_fast[0])
        self.assertEqual(self.data_slow[-1], self.data_fast[-1])
    
    def test_count_spam_messages_consistency(self):
        """Test that both counting methods produce the same result"""
        slow_count = count_spam_messages_slow(self.data_slow)
        fast_count = count_spam_messages_fast(self.data_fast)
        
        self.assertEqual(slow_count, fast_count)
        self.assertEqual(slow_count, 747)
    
    def test_message_lengths_consistency(self):
        """Test that both length calculation methods produce the same result"""
        slow_lengths = get_message_lengths_slow(self.data_slow)
        fast_lengths = get_message_lengths_fast(self.data_fast)
        
        self.assertEqual(len(slow_lengths), len(fast_lengths))
        self.assertEqual(slow_lengths, fast_lengths)
    
    def test_statistics_consistency(self):
        """Test that both statistics methods produce the same result"""
        slow_stats = calculate_statistics_slow(self.data_slow)
        fast_stats = calculate_statistics_fast(self.data_fast)
        
        self.assertEqual(slow_stats['spam_count'], fast_stats['spam_count'])
        self.assertEqual(slow_stats['ham_count'], fast_stats['ham_count'])
        self.assertAlmostEqual(slow_stats['avg_length'], fast_stats['avg_length'], places=2)
        self.assertEqual(slow_stats['max_length'], fast_stats['max_length'])
    
    def test_filter_spam_consistency(self):
        """Test that both filtering methods produce the same result"""
        slow_spam = filter_spam_messages_slow(self.data_slow)
        fast_spam = filter_spam_messages_fast(self.data_fast)
        
        self.assertEqual(len(slow_spam), len(fast_spam))
        self.assertEqual(slow_spam, fast_spam)
    
    def test_counter_analysis(self):
        """Test the Counter-based analysis"""
        label_counts = analyze_with_counter(self.data_fast)
        
        self.assertEqual(label_counts['spam'], 747)
        self.assertEqual(label_counts['ham'], 4825)
    
    def test_data_integrity(self):
        """Test that the loaded data has expected structure"""
        # Check that all rows have at least 2 columns (label and message)
        for row in self.data_fast[:100]:  # Check first 100 rows
            self.assertGreaterEqual(len(row), 2)
            self.assertIn(row[0], ['spam', 'ham'])


class TestPerformanceCharacteristics(unittest.TestCase):
    """Tests to verify performance-related characteristics"""
    
    def test_list_comprehension_creates_single_list(self):
        """Verify that list comprehension is used in optimized version"""
        import inspect
        from data_processor_optimized import load_data_fast
        
        source = inspect.getsource(load_data_fast)
        # List comprehension should be present
        self.assertIn('[', source)
        self.assertIn('for', source)
    
    def test_optimized_uses_join(self):
        """Verify that string join is used in optimized version"""
        import inspect
        from data_processor_optimized import find_long_messages_fast
        
        source = inspect.getsource(find_long_messages_fast)
        self.assertIn('join', source)


if __name__ == '__main__':
    unittest.main()
