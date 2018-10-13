# Answer by Daily Code Mode
def montyHall(doors):
    switch = 1 - ((doors-1)/ doors)
    stick = 1 - switch
    return switch,stick

print(montyHall(4))

# Answer by certis
import random

trials = 1000000
switch = 0
stay   = 0
pick   = 0

for i in range(trials):
    prize = random.randint(0,2)
    if ( pick == prize ):
        stay += 1
    else:
        switch += 1

print(stay, switch)