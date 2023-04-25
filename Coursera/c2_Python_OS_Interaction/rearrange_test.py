#!/usr/bin/env python3

############################################
# Ejercicio: 2-w5-2-testing-unit-tests.py
# Ficheros: rearrange.py y rearrange_test.py
############################################

from rearrange import rearrange_name
import unittest

class Test_Rearrange(unittest.TestCase):
	def test_basic(self):
		testcase = "Lovelace, Ada"
		expected = "Ada Lovelace"
		self.assertEqual(rearrange_name(testcase), expected)

############################################
# Ejercicio: 2-w5-2-testing-edge-cases.py
############################################

	def test_empty(self):
		testcase = ""
		expected = ""
		self.assertEqual(rearrange_name(testcase), expected)

############################################

############################################
# Ejercicio: 2-w5-2-testing-additional-test-cases.py
############################################

	def test_double_name(self):
		testcase = "Hopper, Grace M."
		expected = "Grace M. Hopper"
		self.assertEqual(rearrange_name(testcase), expected)

	def test_one_name(self):
		testcase = "Arthur"
		expected = "Arthur"
		self.assertEqual(rearrange_name(testcase), expected)

############################################

unittest.main()

