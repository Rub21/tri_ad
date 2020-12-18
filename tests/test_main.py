import sys

sys.path.append("..")
import unittest
from tri_ad.main import read_file_sort


class TestSortRows(unittest.TestCase):
    def test_results(self):
        """Test the returned results"""
        # Test maximun value on the list
        self.assertEqual(
            read_file_sort("tests/fixtures/test.txt", 1), [("a54r", 2000)]
        )

        # Test the largest values on the list
        self.assertCountEqual(
            read_file_sort("tests/fixtures/test.txt", 4),
            [("a54r", 2000), ("ceqw", 345), ("aeqe", 234), ("ad45", 234)],
        )

    def test_values(self):
        """Make sure the values are correct"""
        file_url = "https://amp-spacemaps-technical-challenge.s3-ap-northeast-1.amazonaws.com/spacemaps_technical_challenge.txt"

        # Test if large_numbers is negative
        self.assertRaises(ValueError, read_file_sort, file_url, -2)

        # Test if the file not exist locally or int the url
        self.assertRaises(ValueError, read_file_sort, "xyz.txt", 5)
        self.assertRaises(ValueError, read_file_sort, "http://xyz.txt", 5)

        # Test empty file
        self.assertRaises(
            ValueError, read_file_sort, "tests/fixtures/empty.txt", 60
        )
