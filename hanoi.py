def move(f, t):
    print("MOve disc from {} to {}!".format(f,t))
def moveVia(f,v,t):
    move(f,v)# function call to move(): move from step 1 to step2 , out of 3
    #at first, the deestination is v
    move(v,t)# move from step 2 to step 3
    # now the origin is v, and the destination is t
def hanoi(n, f, h, t):
    #n= number of discs
    #f = front position
    #h= helper position
    #t =- target position
    if n == 0:
        pass # this is the base case!
    else:
        hanoi(n-1, f, t, h) # function call WITHIN the funcitondefination!
        move(f, t)
        hanoi(n-1, h, f, t)
hanoi(4, "A", "B", "C")

#based on a tutorial by Professor Thorsten Altenkirch
