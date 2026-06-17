# A. Mystic waves
The pattern of the sequence is simple:

* If n is even, there are equal numbers of x and -x, so the sum is 0.
* If n is odd, there is one extra x, so the sum is x.

t = int(input())

for _ in range(t):
    x, n = map(int, input().split())
    print(x if n % 2 else 0)
