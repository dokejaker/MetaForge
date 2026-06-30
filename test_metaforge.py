# test_metaforge.py
"""
Tests for MetaForge module.
"""

import unittest
from metaforge import MetaForge

class TestMetaForge(unittest.TestCase):
    """Test cases for MetaForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaForge()
        self.assertIsInstance(instance, MetaForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
