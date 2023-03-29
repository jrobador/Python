502. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1

F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Explanation of function syntaxis:

    def fib(self, n: int) -> int:

The def keyword is used to define a function in Python. In this case, the function is a method that belongs to a class (indicated by the self parameter).

The n: int syntax indicates that the n parameter is of type int. This is known as type annotation, which was introduced in Python 3.5 to help developers catch errors early and make their code more readable.

The -> int syntax indicates that the function returns an integer value. This is also a type annotation.

1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

