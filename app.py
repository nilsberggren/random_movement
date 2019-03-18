import random

steps = random.randint(0, 101)
print(steps)

# 0 är center, - är söder och väster på X och Y respektive.
# + är norr och öster på X och Y respektive.
# X är horisontellt
# Y är vertikalt
x = 0
y = 0


def move(x, y):
    # 0 = Söder
    # 1 = Väster
    # 2 = Norr
    # 3 = Öster
    direction = int(random.randint(0, 4))
    if direction == 0:
        y = y - 1
        print("Går ett steg SÖDER")
    elif direction == 1:
        x = x - 1
        print("Går ett steg VÄSTER")
    elif direction == 2:
        y = y + 1
        print("Går ett steg NORR")
    else:
        x = x + 1
        print("Går ett steg ÖSTER")

    return x, y


for i in range(steps):
    x, y = move(x, y)

print(f"Antal steg tagna: {steps}")
print(f"X = {x}")
print(f"Y = {y}")

