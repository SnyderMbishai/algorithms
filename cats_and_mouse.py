"""
Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse doesn't move and the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

You are given q queries in the form of x, y, and z representing the respective positions for cats A and B, and for mouse C. 
Complete the function catAndMouse to return the appropriate answer to each query, which will be printed on a new line.

- If cat A catches the mouse first, print Cat A.
- If cat B catches the mouse first, print Cat B.
- If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.

For example, cat A is at position x=2 and cat B is at y=5. If mouse C is at position z=4, it is 2 units from cat A and 1 unit from cat B. Cat B will catch the mouse.

Function Description:

Complete the catAndMouse function in the editor below. It should return one of the three strings as described.

catAndMouse has the following parameter(s):

x: an integer, Cat A's position
y: an integer, Cat B's position
z: an integer, Mouse C's position

Input Format:

The first line contains a single integer, q, denoting the number of queries.
Each of the q subsequent lines contains three space-separated integers describing the respective values of x (cat A's location),
y (cat B's location), and z (mouse C's location).

Constraints:
- 1 <= q <= 100
- 1 <= x,y,z <= 100

Output Format

For each query, return Cat A if cat A catches the mouse first, Cat B if cat B catches the mouse first, or Mouse C if the mouse escapes.

LINK: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
"""

# first draft
def catAndMouse(x, y, z):
    a = abs(z-x)
    b = abs(z-y)
    if a == b:
        return "Mouse C"
    elif a < b:
        return "Cat A"
    else:
        return "Cat B"

# restructured
def catAndMouse1(x, y, z):
    a = abs(z-x)
    b = abs(z-y)
    return (["Cat A", "Cat B", "Mouse C"][0 if a<b else 1 if b<a else 2 ])

if __name__=='__main__':
    x,y,z = 1,2,3
    print(catAndMouse(x,y,z))
    print(catAndMouse1(x,y,z))
