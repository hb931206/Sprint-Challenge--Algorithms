#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) Linear 0(n) a gets bigger only when N gets bigger

b) N^2 The nested loop

c) 0(1) if bunnies isnt the same thing as N or 0(N) becausse the recursive function growths as n growths

## Exercise II

<!-- Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution. -->

I would use a techniques from the binary search where f would be the half way point of the building n. Eggs dropped from above f would break and eggs wouldn't break if dropped from below.

My solution is log(n)

<!-- def binary_search(n, f, drop:
broken = 0
alive = 0

 f = n//2

    if drop > n[f]:
        broken+=1

    if target < n[f]:
        alive +=1

    return "The number of live eggs were X and the broken eggs are Y at height F
