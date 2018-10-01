import unittest


class FibonacciTest(unittest.TestCase):

    def fib(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

    def testCalculation(self):
        self.assertEqual(self.fib(0), 0)
        self.assertEqual(self.fib(1), 1)
        self.assertEqual(self.fib(5), 5)
        self.assertEqual(self.fib(10), 55)
        self.assertEqual(self.fib(20), 6765)

if __name__ == "__main__":
    unittest.main()