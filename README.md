# Reduceit
Dave has been obsessed with a game 2048. His younger brother Larry is a noob and cannot comprehend the intricate logic behind this game. To help him, Dave simplifies the game.

Larry is provided with N integers and it is given that all of them are in the form 2^x. where x is any whole number. His task at hand is similar i.e he has to find the final set of numbers so that they cannot be further merged can be obtained by merging those numbers. You have to make sure that the sum of this set of numbers is maximum.

The numbers can be merged only if they are the same. For example:
If you are given the numbers 2 2 4 8 16
Then you can get the set (32).

If you are given the numbers 2 4 4 8 8 16 32 32.
Then you can get the set (2, 8, 32, 64).
Larry is still confused and requests you to make a program that will find him the answer.

INPUT:
The first line is an integer N: the size of the original set.
The second line contains N integers: the members of the set.

OUTPUT:
It should be one line containing all the elements of the merged set.

EXAMPLES

Input

5
224816

Output

32

Input

8 
2 4 4 8 8 16 32 32

Output

28 32 64
