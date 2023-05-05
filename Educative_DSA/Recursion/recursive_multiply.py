def rec_multiply(x, y):

    # This cuts down on the total number of
    # recursive calls:
    if x < y:
        return rec_multiply(y, x)
    if y == 0:
        return 0
    return x + rec_multiply(x, y-1)

x = 500
y = 2000

print(rec_multiply(x,y))