# The Fibonacci sequence is the integer sequence defined by the recurrence relation:
# F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. In other words, the nth Fibonacci
# number is the sum of the prior two Fibonacci numbers. Below are the first few values of
# the sequence:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

# Given a number n, print the n-th Fibonacci Number.

class Solution():
    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)


n = 9
print(Solution().fibonacci(n))
