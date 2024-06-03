The recursive Fibonacci function works by breaking down the problem of finding the `n`-th Fibonacci number into smaller subproblems, specifically finding the (`n-1`)-th and (`n-2`)-th Fibonacci numbers, and then summing these results. Here's a step-by-step explanation of how it sums the answers:

1. **Base Cases:**
   - If `n` is 1, the function returns 0. This is the first Fibonacci number.
   - If `n` is 2, the function returns 1. This is the second Fibonacci number.

2. **Recursive Case:**
   - For `n` greater than 2, the function calls itself twice: once with `n-1` and once with `n-2`.
   - These two recursive calls will, in turn, break down into further recursive calls until they reach the base cases.
   - The results of these two calls are then summed to get the Fibonacci number for `n`.

Let's see an example with `n = 5` to illustrate how the sum is computed:

```python
fibonacci(5)
```

1. `fibonacci(5)` calls `fibonacci(4)` and `fibonacci(3)`.
2. `fibonacci(4)` calls `fibonacci(3)` and `fibonacci(2)`.
   - `fibonacci(2)` returns 1.
   - `fibonacci(3)` calls `fibonacci(2)` and `fibonacci(1)`.
     - `fibonacci(2)` returns 1.
     - `fibonacci(1)` returns 0.
     - `fibonacci(3)` returns 1 + 0 = 1.
   - `fibonacci(4)` returns 1 + 1 = 2.
3. `fibonacci(3)` calls `fibonacci(2)` and `fibonacci(1)`.
   - `fibonacci(2)` returns 1.
   - `fibonacci(1)` returns 0.
   - `fibonacci(3)` returns 1 + 0 = 1.
4. `fibonacci(5)` returns 2 + 1 = 3.

So, the function recursively breaks down the problem into smaller subproblems, solves each subproblem, and combines the results to get the final answer.

Here's a more detailed breakdown of the recursive calls for `fibonacci(5)`:

```
fibonacci(5)
= fibonacci(4) + fibonacci(3)
= (fibonacci(3) + fibonacci(2)) + (fibonacci(2) + fibonacci(1))
= ((fibonacci(2) + fibonacci(1)) + fibonacci(2)) + (fibonacci(2) + fibonacci(1))
= ((1 + 0) + 1) + (1 + 0)
= (1 + 1) + 1
= 2 + 1
= 3
```

Each call to `fibonacci` breaks the problem down into smaller pieces until reaching the base cases, and then the results are combined to form the final answer.