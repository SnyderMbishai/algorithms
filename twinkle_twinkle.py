import re


def twinkle(s):
    pass


msg = """Twinkle, twinkle, little star, 
How I wonder what you are! Up above the world so high, 
Like a diamond in the sky. Twinkle, twinkle, little star, 
How I wonder what you are"""
print(len(msg.split(" ")[:32]), "msg")
print(msg.split(" ")[:32], "222222")
x = re.findall("[A-Z][^A-Z]*", msg)
y = msg.split("H")
print(x, "reeee")
print(y, "yyy")
twinkle(msg)
