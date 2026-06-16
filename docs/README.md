# Asymptotic Analysis
For **time complexity**, count the number of fundamental operations as a function of input size \(n\): comparisons, arithmetic, array accesses, hash lookups, recursive calls, and loop iterations. The exact operation you choose usually does not matter as long as it represents the dominant work consistently. [youtube](https://www.youtube.com/watch?v=2dRyV7k3XZM)

For **space complexity**, count the extra memory used beyond the input itself: temporary variables, auxiliary arrays, recursion stack depth, and any additional data structures created during execution. In interviews and most DSA contexts, “space complexity” usually means **auxiliary space**, not the input storage itself. [medium](https://medium.com/@messages2kaushik/understanding-space-and-time-complexity-in-algorithms-what-how-and-why-b7a302a84abb)

## What matters most

Use these factors when analyzing an algorithm:

- Input size, because complexity is defined as growth with respect to input size. [geeksforgeeks](https://www.geeksforgeeks.org/dsa/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/)
- Loop structure, especially nested loops and how many times each runs. [medium](https://medium.com/@pnandhiniofficial/time-and-space-complexity-a-beginners-guide-88d617d29d01)
- Recursion depth and work per call, because stack usage affects space and repeated calls affect time. [medium](https://medium.com/@messages2kaushik/understanding-space-and-time-complexity-in-algorithms-what-how-and-why-b7a302a84abb)
- Data structure operations, since arrays, hash maps, trees, and heaps have different costs. [askfilo](https://askfilo.com/user-question-answers-smart-solutions/what-are-the-factors-that-influence-time-and-space-3330393438323933)
- Best, average, and worst case behavior, because the same algorithm can behave differently depending on input. [cs.cornell](https://www.cs.cornell.edu/courses/cs312/2004fa/lectures/lecture16.htm)

## What to ignore

In asymptotic analysis, you usually ignore:

- Constant factors, like \(3n\) vs \(100n\), because they do not change growth class. [pages.cs.wisc](https://pages.cs.wisc.edu/~hasti/cs240/readings/10_Asymptotic_Analysis.pdf)
- Lower-order terms, like \(n^2 + n\), because \(n^2\) dominates as \(n\) grows. [personal.math.ubc](https://personal.math.ubc.ca/~wetton/notes/lecture6.pdf)
- Small-input behavior, because asymptotic analysis is about large-scale growth. [cs.cmu](https://www.cs.cmu.edu/afs/cs/academic/class/15210-f25/www/algobook/analysis/asymptotics.pdf)
- Hardware differences, compiler optimizations, and actual wall-clock runtime, because those are implementation-dependent rather than algorithmic. [askfilo](https://askfilo.com/user-question-answers-smart-solutions/what-are-the-factors-that-influence-time-and-space-3330393438323933)

## How to analyze correctly

A good workflow is:

1. Define the input size clearly.  
2. Identify the dominant operation.  
3. Count how many times that operation runs in the worst case.  
4. Multiply by the cost of the operation if it is not \(O(1)\).  
5. Drop constants and lower-order terms. [youtube](https://www.youtube.com/watch?v=MUiDz2fAqeI)

For example, one loop over \(n\) items is \(O(n)\), two nested loops over \(n\) items is usually \(O(n^2)\), and a recursive algorithm that halves the problem each time is often \(O(\log n)\) or \(O(n \log n)\) depending on the work per level. [people.orie.cornell](https://people.orie.cornell.edu/vc333/orie5270/lectures/03/)

## Common mistakes

A lot of bad complexity analysis comes from these mistakes:

- Confusing output size with input size.
- Counting only the outer loop and ignoring expensive work inside it.
- Treating the number of digits or factors in a number as the same thing as the value of the number.
- Assuming recursive calls are free.
- Analyzing runtime based on a specific test case instead of the general case. [medium](https://medium.com/@pnandhiniofficial/time-and-space-complexity-a-beginners-guide-88d617d29d01)

## A useful mental rule

Ask: “If the input gets 10 times bigger, what part of the algorithm grows the fastest?”  
That is the part that defines the asymptotic complexity. If two costs grow at different rates, the faster-growing one eventually dominates. [cs.cmu](https://www.cs.cmu.edu/afs/cs/academic/class/15210-f25/www/algobook/analysis/asymptotics.pdf)

## Space analysis example

If a function uses a few variables and no extra structures, that is usually \(O(1)\) auxiliary space. If it builds a list of size \(n\), that is \(O(n)\) space. If it uses recursion with depth \(n\), the call stack alone can make it \(O(n)\) space. [youtube](https://www.youtube.com/watch?v=2dRyV7k3XZM)
