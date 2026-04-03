# test_cloudsecureapi.py
"""
Tests for CloudSecureApi module.
"""

import unittest
from cloudsecureapi import CloudSecureApi

class TestCloudSecureApi(unittest.TestCase):
    """Test cases for CloudSecureApi class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CloudSecureApi()
        self.assertIsInstance(instance, CloudSecureApi)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CloudSecureApi()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
