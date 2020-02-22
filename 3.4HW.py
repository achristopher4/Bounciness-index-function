
import math

height = int(input("Enter the height from which the ball is dropped: "))
index = float(input("Enter the bounciness index of the ball: "))
bounce = int(input("Enter the number of times the ball is allowed to continue bouncing:"))

total = 0
x = height

for count in range(bounce):
    y = x
    x = y * index
    z = x + y
    total = total + z

print(total)
