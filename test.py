import unittest
import re
import os
import pattern as p
pattern = p.pattern
class Test_ECKS_DEE(unittest.TestCase):
    
    def setUp(self) -> None:
        
        return super().setUp()
    def test_allLowerCases(self):
        self.assertTrue(re.search(pattern, "xd", re.IGNORECASE))
    def test_allUpperCases(self):
        self.assertTrue(re.search(pattern, "XD", re.IGNORECASE))
    def test_nextToPeriod(self):
        self.assertTrue(re.search(pattern, "XD.", re.IGNORECASE))
    def test_extraD(self):
        self.assertFalse(re.search(pattern, "XDD", re.IGNORECASE))
    def test_multiLine(self):
        self.assertTrue(re.search(pattern, """
        I know Ecks Dee is longer than XD
        But I like to use it nontheless
        Because it is quirky.
        """, re.IGNORECASE))
    def test_aSubStringInOtherWords(self):
        self.assertFalse(re.search(pattern, "axdx", re.IGNORECASE))