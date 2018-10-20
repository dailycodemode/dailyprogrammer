rows = 5
columns = 4

print("*" + "*" * 3 * columns + "*")
for row in range(rows):
    print("*", end="")
    for column in range(columns):
        if (column + row)%2 == 0: print(black, end="")
        else: print(white, end="")
    print("*")
print("*" + "*" * 3 * columns + "*")

# ANSWER by juanfeng

def printer(rows, cols, width, height, solid, blank):
    print((((solid * width + blank * width) * cols)[:cols * width]  + '\n') * height)
    if rows > 1: printer(rows - 1, cols, width, height, blank, solid)
printer(5, 3, 2, 2, '#', ' ')

# BREAKDOWN
# juanfen's answer is a lot more complex than mine or the second answer. The best way to
# break this apart into seperate line's to try and see what is happening.

def printer(rows, cols, width, height, solid, blank):
    print((((solid * width + blank * width) * cols) \
               [:cols * width] \
           + '\n') * height)

    if rows > 1: printer(rows - 1, cols, width, height, blank, solid)
printer(5, 3, 2, 2, '#', ' ')

line one writes out a generic board space and then multiplies this by the amount of columns
This is a string so the juanfeng then says to limit how far the each line will go [:cols * width]
it then adds a new line to the end of the string which will allow him to repeat the same line when
he multiplies by the height

he then calls the function on itself but reverses the blanks and solids
which gives the mesh appearance whilst iterating through the rows.

SUMMARY
a stunning piece of code from juanfen who has really understood what can be done here.

