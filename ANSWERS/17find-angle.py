import math
a=int(input())
b=int(input())
angle=math.atan(a/b)
print(round((math.degrees(angle))),chr(176),sep="")
