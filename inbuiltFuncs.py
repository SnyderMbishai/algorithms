# hash()
a = "Hello World!"
aa = "Hello World!"
b = 12.5
c = ("a", "b", "c")

print(hash(a), hash(aa), hash(b), hash(c), hash(a) == hash(aa))


# map()
def square(n):
    return n * n


print(list(map(square, [1, 2, 3, 4, 5])))

# zip()
nms = [
    1,
    2,
    3,
]
s = ["a", "b", "c"]
print(set(zip(nms, s)))
print(dict(zip(nms, s)))
print(list(zip(nms, s)))

# eval()
r1 = eval("2 + 4")
r2 = eval("2*4")
print(r1, r2)

# split()
t1 = "aaaa#bbbb#ccc"
t2 = "ssss dddd gggg"
print(t1.split("#"))
print(t2.split(" "))

# ord()
o1 = ord("a")
o2 = ord("$")
o3 = ord(" ")
print(o1, o2, o3)


# dir()
class User:
    name = "name"
    age = 10
    no = 21


print(dir(User))

# pow()
p = pow(2, 3)
p1 = pow(3, 3)
p2 = 3**3
print(p, p1, p2)
