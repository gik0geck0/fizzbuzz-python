import unittest
from fizzbuzz import handleValue

# Run this using `python3 fizzbuzz.test.py`
# OR
# python -m unittest
#
# NOTE: unittest is directory (package) sensitive, so the location of this file relative to the subject & the directory from which you run it are important

class FizzBuzzTest(unittest.TestCase):
	def run_cases(self, cases):
		for case in cases:
			actual = handleValue(case[0], case[1], case[2])
			self.assertEqual(actual, case[3], "Expected x=%i, y=%i, i=%i to produce %s but got %s" % (case + (actual,)) )

	# Bounds defined by the problem:
	# 1 <= X < Y <= N <= 100
	def test_i_bounds(self):
		cases = [
			# x, y, i, expected
			(1, 1, 1, "FizzBuzz"),
			(1, 2, 1, "Fizz"),
			(1, 2, 2, "FizzBuzz"),
			(2, 3, 100, "Fizz"),
			(3, 3, 100, "100"),
			(99, 100, 99, "Fizz"),
			(99, 100, 100, "Buzz"),
			(2, 3, 1, "1"),
			(2, 3, 7, "7"),
			(2, 4, 1, "1"),
			(3, 5, 1, "1")
		]
		self.run_cases(cases)

	def test_fizz(self):
		cases = [
			# x, y, i, expected
			(2, 3, 2, "Fizz"),
			(2, 3, 4, "Fizz"),
		]
		self.run_cases(cases)

	def test_buzz(self):
		cases = [
			(2, 3, 3, "Buzz"),
			(2, 3, 9, "Buzz"),
			(3, 5, 5, "Buzz"),
			(3, 5, 10, "Buzz")
		]
		self.run_cases(cases)
	
	def test_fizzbuzz(self):
		cases = [
			(2, 3, 6, "FizzBuzz"),
			(2, 4, 4, "FizzBuzz"),
			(3, 5, 15, "FizzBuzz")
		]
		self.run_cases(cases)

if __name__ == '__main__':
    unittest.main()
